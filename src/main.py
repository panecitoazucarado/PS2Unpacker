import os
import sys
import datetime
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, 
                             QFileDialog, QListWidget, QLabel, QMenuBar, QMenu, 
                             QAction, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class RomDecompApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setup_initial_state()
        
    def setup_initial_state(self):
        self.compilation_datetime = datetime.datetime.now()
        self.compilation_number = self.compilation_datetime.strftime("%Y%m%d%H%M%S")
        self.modules = []
        self.romfile = None

    def setup_ui(self):
        self.setWindowTitle("PS2 Unpacker")
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(QIcon("/Users/heidycolszewski/Desktop/app bios/assets/iconos/icon.icns"))
        
        layout = QVBoxLayout()
        self.create_menu_bar(layout)
        self.create_file_ui(layout)
        self.create_module_ui(layout)
        self.create_extraction_buttons(layout)
        self.setLayout(layout)

    def create_menu_bar(self, layout):
        menubar = QMenuBar(self)
        
        # Menú Archivo
        file_menu = QMenu("Archivo", self)
        file_menu.addAction("Importar .rom0", lambda: self.open_file("rom0"))
        file_menu.addAction("Importar .bin", lambda: self.open_file("bin"))
        menubar.addMenu(file_menu)

        # Menú Ayuda
        help_menu = QMenu("Ayuda", self)
        help_menu.addAction("Acerca de", self.show_about)
        menubar.addMenu(help_menu)

        layout.setMenuBar(menubar)

    def create_file_ui(self, layout):
        self.file_label = QLabel("Selecciona un archivo ROM", self)
        self.open_btn = QPushButton("Abrir archivo ROM", self)
        self.open_btn.clicked.connect(self.open_file)
        layout.addWidget(self.file_label)
        layout.addWidget(self.open_btn)

    def create_module_ui(self, layout):
        self.module_list = QListWidget(self)
        layout.addWidget(self.module_list)

    def create_extraction_buttons(self, layout):
        self.extract_all_btn = QPushButton("Extraer todos los módulos", self)
        self.extract_all_btn.clicked.connect(self.extract_all)
        self.extract_one_btn = QPushButton("Extraer módulo seleccionado", self)
        self.extract_one_btn.clicked.connect(self.extract_selected)
        layout.addWidget(self.extract_all_btn)
        layout.addWidget(self.extract_one_btn)

    def show_about(self):
        about_info = f"""
        <h3>PS2-ROM-DESEMPAQUETADOR-DE-BIOS</h3>
        <p><b>Desarrollador:</b> Panecito Azucarado</p>
        <p><b>Versión:</b> {self.compilation_number}</p>
        <p><b>Compilación:</b> {self.compilation_datetime.strftime("%Y-%m-%d %H:%M:%S")}</p>
        """
        QMessageBox.about(self, "Acerca de", about_info)

    def open_file(self, file_type=None):
        filters = {
            "rom0": "Archivos ROM0 (*.rom0);;Todos los archivos (*)",
            "bin": "Archivos Binarios (*.bin);;Todos los archivos (*)",
            None: "Archivos Binarios (*.bin);Archivos ROM0 (*.rom0);Todos los archivos (*)"
        }
        
        file, _ = QFileDialog.getOpenFileName(
            self, 
            "Seleccionar archivo ROM", 
            "", 
            filters.get(file_type, filters[None])
        )
        
        if file:
            self.process_file(file)

    def process_file(self, file_path):
        try:
            self.clear_previous_data()
            self.romfile = self.open_rom_file(file_path)
            romdir_info = self.find_romdir()
            
            if not romdir_info:
                raise ValueError("Estructura ROMDIR no encontrada")
                
            self.modules = self.parse_romdir(romdir_info)
            self.update_module_list()
            
        except Exception as e:
            self.handle_error(f"Error procesando archivo:\n{str(e)}")
            self.clear_resources()

    def clear_previous_data(self):
        self.module_list.clear()
        self.modules = []
        if self.romfile:
            self.romfile.close()

    def open_rom_file(self, path):
        print(f"Abriendo: {path}")
        return open(path, 'rb')

    def find_romdir(self):
        self.romfile.seek(0)
        file_size = os.fstat(self.romfile.fileno()).st_size
        
        for _ in range(file_size):
            if self.romfile.read(1)[0] == 0x52:
                next_bytes = list(self.romfile.read(4))
                if next_bytes == [0x45, 0x53, 0x45, 0x54]:
                    position = self.romfile.tell() - 5
                    reset_size = self.read_size(position + 0x0C)
                    romdir_size = self.read_size(position + 0x1C)
                    return (position, romdir_size)
        return None

    def read_size(self, offset):
        self.romfile.seek(offset)
        return int.from_bytes(self.romfile.read(4), byteorder='little')

    def parse_romdir(self, romdir_info):
        modules = []
        self.romfile.seek(romdir_info[0])
        
        for _ in range((romdir_info[1] // 16) - 1):
            module_name = self.romfile.read(10).decode('ascii', errors='ignore').strip('\x00')
            self.romfile.seek(self.romfile.tell() + 2)
            module_size = self.align_size(self.read_size(self.romfile.tell()))
            modules.append((module_name, module_size))
        
        return modules

    def align_size(self, size):
        return size + (16 - size % 16) if size % 16 != 0 else size

    def update_module_list(self):
        for idx, (name, _) in enumerate(self.modules):
            self.module_list.addItem(f"{idx}. {name}")

    def extract_all(self):
        if not self.validate_extraction():
            return
            
        success, failures = 0, []
        extraction_path = self.get_extraction_path()
        
        for idx in range(len(self.modules)):
            try:
                self.save_module(idx, extraction_path)
                success += 1
            except Exception as e:
                failures.append(str(idx))
        
        self.show_extraction_report(success, failures)

    def extract_selected(self):
        if not self.validate_extraction():
            return
            
        selected = self.module_list.selectedItems()
        if selected:
            idx = int(selected[0].text().split('.')[0])
            try:
                path = self.save_module(idx, self.get_extraction_path())
                QMessageBox.information(self, "Éxito", f"Módulo {idx} extraído:\n{path}")
            except Exception as e:
                self.handle_error(f"Error extrayendo módulo {idx}:\n{str(e)}")

    def validate_extraction(self):
        if not self.romfile or self.romfile.closed:
            self.handle_error("No hay archivo ROM cargado")
            return False
        if not self.modules:
            self.handle_error("No hay módulos para extraer")
            return False
        return True

    def get_extraction_path(self):
        path = os.path.join(os.path.expanduser("~/Downloads"), "extraction_bios")
        os.makedirs(path, exist_ok=True)
        return path

    def save_module(self, index, output_dir):
        module_name, module_size = self.modules[index]
        self.romfile.seek(self.calculate_offset(index))
        
        output_path = os.path.join(output_dir, f"module_{index}_{module_name}.bin")
        with open(output_path, "wb") as f:
            f.write(self.romfile.read(module_size))
        
        return output_path

    def calculate_offset(self, index):
        return sum(size for _, size in self.modules[:index])

    def show_extraction_report(self, success, failures):
        report = f"Módulos extraídos exitosamente: {success}"
        if failures:
            report += f"\nMódulos con errores: {', '.join(failures)}"
        
        QMessageBox.information(
            self,
            "Proceso completado",
            report,
            QMessageBox.Ok
        )

    def handle_error(self, message):
        QMessageBox.critical(self, "Error", message)

    def clear_resources(self):
        if self.romfile:
            self.romfile.close()
        self.romfile = None
        self.modules = []

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RomDecompApp()
    window.show()
    sys.exit(app.exec_())