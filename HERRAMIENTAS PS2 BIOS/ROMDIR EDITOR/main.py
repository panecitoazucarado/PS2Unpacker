import sys
import struct
import shutil
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class RomdirEntry:
    def __init__(self, name, ext_info_size, file_size, start_address):
        self.name = name
        self.ext_info_size = ext_info_size
        self.file_size = file_size
        self.start_address = start_address

    def to_bytes(self):
        name_bytes = self.name.ljust(10, '\x00').encode('ascii')[:10]
        return name_bytes + struct.pack("<HI", self.ext_info_size, self.file_size)

class RomModel(QAbstractTableModel):
    def __init__(self, entries):
        super().__init__()
        self.headers = ["Archivo", "Tamaño", "Dirección", "Ext Info"]
        self.entries = entries
        self.original_entries = entries.copy()

    def rowCount(self, parent=None):
        return len(self.entries)

    def columnCount(self, parent=None):
        return 4

    def data(self, index, role):
        entry = self.entries[index.row()]
        col = index.column()
        
        if role == Qt.ItemDataRole.DisplayRole:
            if col == 0: return entry.name
            if col == 1: return f"{entry.file_size} bytes"
            if col == 2: return f"0x{entry.start_address:08X}"
            if col == 3: return entry.ext_info_size

        if role == Qt.ItemDataRole.EditRole:
            if col == 0: return entry.name
            if col == 1: return entry.file_size
            if col == 3: return entry.ext_info_size

        if role == Qt.ItemDataRole.ForegroundRole:
            return QColor("#008000") if col == 2 else QColor("#000080")

        if role == Qt.ItemDataRole.TextAlignmentRole:
            return Qt.AlignmentFlag.AlignRight if col > 0 else Qt.AlignmentFlag.AlignLeft

        if role == Qt.ItemDataRole.BackgroundRole:
            return QColor("#f0f0f0") if index.row() % 2 else QColor("#e0e0e0")

        if role == Qt.ItemDataRole.ToolTipRole:
            original = self.original_entries[index.row()]
            return f"Original: {original.name} | Tamaño: {original.file_size}"

    def setData(self, index, value, role):
        if role != Qt.ItemDataRole.EditRole:
            return False

        entry = self.entries[index.row()]
        col = index.column()
        
        try:
            if col == 0:
                if len(value) > 10:
                    raise ValueError("Máximo 10 caracteres")
                entry.name = value
            elif col == 1:
                new_size = int(value.replace(' bytes', ''))
                if new_size < 0:
                    raise ValueError("Tamaño inválido")
                entry.file_size = new_size
            elif col == 3:
                entry.ext_info_size = int(value)
                
            self.dataChanged.emit(index, index)
            return True
        except Exception as e:
            QMessageBox.warning(self.parent(), "Error", str(e))
            return False

    def flags(self, index):
        return super().flags(index) | Qt.ItemFlag.ItemIsEditable

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self.headers[section]
        return None

class HexViewer(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setFont(QFont("Courier New", 10))
        
    def display(self, data, offset=0):
        self.clear()
        while offset < len(data):
            line = data[offset:offset+16]
            hex_str = ' '.join(f"{b:02X}" for b in line)
            text_str = ''.join(chr(b) if 32 <= b < 127 else '.' for b in line)
            self.append(f"{offset:08X}  {hex_str.ljust(47)}  {text_str}")
            offset += 16

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PS2 ROMDIR Editor Pro v5.1")
        self.setGeometry(100, 100, 1400, 900)
        
        # Componentes UI
        self.table = QTableView()
        self.hex_view = HexViewer()
        self.status = QStatusBar()
        self.progress = QProgressBar()
        self.progress.setVisible(False)
        
        # Configuración de seguridad
        self.backup_dir = "backups"
        self.current_file = None
        self.original_data = None
        
        self.init_ui()

    def init_ui(self):
        # Configuración de tabla
        self.table.setAlternatingRowColors(True)
        self.table.setSortingEnabled(False)
        self.table.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.show_context_menu)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        # Diseño
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(self.table)
        splitter.addWidget(self.hex_view)
        splitter.setSizes([600, 400])
        
        # Menú
        menu = self.menuBar()
        file_menu = menu.addMenu("Archivo")
        edit_menu = menu.addMenu("Editar")
        tools_menu = menu.addMenu("Herramientas")
        
        # Acciones
        self.open_action = QAction("Abrir ROMDIR", self)
        self.open_action.setShortcut(QKeySequence("Ctrl+O"))
        self.open_action.triggered.connect(self.open_file)
        
        self.save_action = QAction("Guardar ROMDIR", self)
        self.save_action.setShortcut(QKeySequence("Ctrl+S"))
        self.save_action.setEnabled(False)
        self.save_action.triggered.connect(self.save_file)
        
        self.backup_action = QAction("Crear Backup", self)
        self.backup_action.setShortcut(QKeySequence("Ctrl+B"))
        self.backup_action.setEnabled(False)
        self.backup_action.triggered.connect(self.create_backup)
        
        self.add_action = QAction("Agregar entrada", self)
        self.add_action.setShortcut(QKeySequence("Ctrl+N"))
        self.add_action.setEnabled(False)
        self.add_action.triggered.connect(self.add_entry)
        
        self.remove_action = QAction("Eliminar entrada", self)
        self.remove_action.setShortcut(QKeySequence("Del"))
        self.remove_action.setEnabled(False)
        self.remove_action.triggered.connect(self.remove_entry)
        
        self.validate_action = QAction("Validar ROMDIR", self)
        self.validate_action.setShortcut(QKeySequence("Ctrl+V"))
        self.validate_action.setEnabled(False)
        self.validate_action.triggered.connect(self.validate_romdir)
        
        file_menu.addActions([self.open_action, self.save_action, self.backup_action])
        edit_menu.addActions([self.add_action, self.remove_action])
        tools_menu.addAction(self.validate_action)
        
        # Configuración final
        self.setCentralWidget(splitter)
        self.setStatusBar(self.status)
        self.status.addPermanentWidget(self.progress)
        self.table.doubleClicked.connect(self.show_hex)
        
        # Inicialización
        self._update_actions(False)

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Abrir BIOS/ROMDIR", "", "Archivos BIN (*.bin *.BIN *.bak)"
        )
        if not path:
            return
            
        try:
            # Crear copia de seguridad
            backup_path = self.create_backup(path)
            
            # Convertir a .bak si es necesario
            if not path.lower().endswith('.bak'):
                new_path = path.replace('.bin', '.bak') if '.bin' in path else path + '.bak'
                shutil.copy2(path, new_path)
                path = new_path
                self.status.showMessage(f"Convertido a formato seguro: {path}")
            
            with open(path, "rb") as f:
                self.original_data = f.read()
            
            # Buscar RESET en toda la memoria
            reset_pos = self.original_data.find(b"RESET\x00\x00\x00\x00\x00")
            if reset_pos == -1:
                reset_pos = self.original_data.find(b"RESET")
                if reset_pos == -1:
                    raise ValueError("Formato de ROMDIR no reconocido")
                QMessageBox.warning(self, "Advertencia",
                    "Archivo extraído mediante volcado de memoria detectado. "
                    "Se intentará cargar pero podría contener errores.")
            
            self.entries = []
            offset = reset_pos
            cumulative_size = 0
            
            while True:
                chunk = self.original_data[offset:offset+16]
                if len(chunk) < 16:
                    break
                    
                name = chunk[:10].split(b'\x00')[0].decode('ascii', errors='replace')
                ext_info = struct.unpack("<H", chunk[10:12])[0]
                size = struct.unpack("<I", chunk[12:16])[0]
                
                entry = RomdirEntry(
                    name,
                    ext_info,
                    size,
                    reset_pos + cumulative_size
                )
                self.entries.append(entry)
                cumulative_size += size
                offset += 16

            self.model = RomModel(self.entries)
            self.table.setModel(self.model)
            self.current_file = path
            self._update_actions(True)
            self.status.showMessage(f"Cargado: {path} ({len(self.entries)} archivos)")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Archivo inválido: {str(e)}")

    def create_backup(self, path):
        bak_path = path.replace('.bin', '.bak') if '.bin' in path else path + '.bak'
        shutil.copy2(path, bak_path)
        self.status.showMessage(f"Backup creado: {bak_path}")
        return bak_path

    def save_file(self):
        if not self.current_file or not self.model:
            return
            
        if not self.validate_romdir(silent=True):
            QMessageBox.warning(self, "Error", "ROMDIR inválido - corrija errores primero")
            return
            
        reply = QMessageBox.warning(self, "Confirmar", 
            "¿Está seguro de guardar los cambios? Esto modificará el archivo .bak",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            
        if reply != QMessageBox.StandardButton.Yes:
            return
            
        try:
            # Recalcula direcciones
            current_pos = self.entries[0].start_address
            for entry in self.model.entries:
                entry.start_address = current_pos
                current_pos += entry.file_size

            # Encuentra posición original del ROMDIR
            romdir_start = self.original_data.find(b"RESET\x00\x00\x00\x00\x00")
            romdir_data = b''.join([entry.to_bytes() for entry in self.model.entries])
            
            # Escribe de forma segura
            with open(self.current_file, "r+b") as f:
                f.seek(romdir_start)
                f.write(romdir_data)
                
                # Verificación
                f.seek(romdir_start)
                written = f.read(len(romdir_data))
                if written != romdir_data:
                    raise ValueError("Verificación fallida")

            self.model.original_entries = self.model.entries.copy()
            QMessageBox.information(self, "Éxito", "ROMDIR guardado correctamente")
            self.status.showMessage("Archivo .bak actualizado con éxito")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al guardar: {str(e)}")

    def validate_romdir(self, silent=False):
        errors = []
        required = {"RESET", "ROMDIR", "EXTINFO", "ROMVER"}
        names = {entry.name for entry in self.model.entries}
        
        # Verificar entradas requeridas
        missing = required - names
        if missing:
            errors.append(f"Faltan entradas obligatorias: {', '.join(missing)}")
        
        # Verificar direcciones
        previous_end = self.model.entries[0].start_address
        for i, entry in enumerate(self.model.entries[1:], 1):
            if entry.start_address < previous_end:
                errors.append(f"Superposición en entrada {i}: {entry.name}")
            previous_end = entry.start_address + entry.file_size
        
        # Verificar nombres
        for entry in self.model.entries:
            if len(entry.name) > 10:
                errors.append(f"Nombre inválido: {entry.name}")
        
        if not silent:
            if errors:
                QMessageBox.warning(self, "Validación", "\n".join(errors))
            else:
                QMessageBox.information(self, "Validación", "ROMDIR válido")
        return not bool(errors)

    def show_hex(self, index):
        entry = self.model.entries[index.row()]
        data = self.original_data[entry.start_address:entry.start_address+entry.file_size]
        self.hex_view.display(data, entry.start_address)

    def show_context_menu(self, pos):
        menu = QMenu()
        menu.addAction(self.add_action)
        menu.addAction(self.remove_action)
        menu.exec(self.table.viewport().mapToGlobal(pos))

    def add_entry(self):
        new_entry = RomdirEntry("NUEVO", 0, 0, 0)
        self.model.beginInsertRows(QModelIndex(), len(self.model.entries), len(self.model.entries))
        self.model.entries.append(new_entry)
        self.model.endInsertRows()
        self._update_actions(True)

    def remove_entry(self):
        indexes = self.table.selectedIndexes()
        if not indexes:
            return
            
        row = indexes[0].row()
        self.model.beginRemoveRows(QModelIndex(), row, row)
        del self.model.entries[row]
        self.model.endRemoveRows()
        self._update_actions(True)

    def _update_actions(self, enabled):
        self.save_action.setEnabled(enabled)
        self.backup_action.setEnabled(enabled)
        self.add_action.setEnabled(enabled)
        self.remove_action.setEnabled(enabled)
        self.validate_action.setEnabled(enabled)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())