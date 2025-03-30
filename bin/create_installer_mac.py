#!/usr/bin/env python3
import os
import shutil
import subprocess
from pathlib import Path

class MacOSInstaller:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent
        self.build_dir = self.project_root / "dist" / "mac"
        self.pkg_dir = self.build_dir / "pkg"
        self.app_name = "PS2Unpacker"
        self.version = "1.0.0"
        
    def build_package(self):
        """Construye el paquete .pkg para macOS"""
        print("🛠  Construyendo paquete de instalación para macOS...")
        
        # 1. Preparar directorios
        self._prepare_directories()
        
        # 2. Compilar aplicación
        self._build_app()
        
        # 3. Mover la aplicación compilada
        self._move_compiled_app()
        
        # 4. Crear distribución
        self._create_distribution()
        
        # 5. Firmar paquete (opcional)
        self._sign_package()
        
        print(f"\n✅ Instalador creado en: {self.build_dir/'PS2Unpacker.pkg'}")

    def _prepare_directories(self):
        """Prepara la estructura de directorios"""
        dirs = [
            self.build_dir,
            self.pkg_dir,
            self.pkg_dir / "scripts",
            self.pkg_dir / f"{self.app_name}.app/Contents/MacOS",
            self.pkg_dir / f"{self.app_name}.app/Contents/Resources"
        ]
        
        for d in dirs:
            try:
                d.mkdir(parents=True, exist_ok=True)
                print(f"📂 Directorio listo: {d}")
            except Exception as e:
                print(f"⚠️  Error creando directorio {d}: {str(e)}")
                raise

    def _build_app(self):
        """Compila la aplicación usando PyInstaller directamente"""
        print("🔨 Compilando aplicación con PyInstaller...")
        
        # Configuración de PyInstaller
        pyinstaller_cmd = [
            "pyinstaller",
            "--noconfirm",
            "--windowed",
            "--name", self.app_name,
            "--icon", str(self.project_root / "src" / "resources" / "icons" / "macos" / "app.icns"),
            "--osx-bundle-identifier", f"com.ps2unpacker.{self.app_name}",
            "--add-data", f"{self.project_root / 'src' / 'resources' / 'icons'}:resources/icons",
            "--add-data", f"{self.project_root / 'src' / 'resources' / 'qss'}:resources/qss",
            "--add-data", f"{self.project_root / 'src' / 'resources' / 'translations'}:resources/translations",
            "--distpath", str(self.build_dir),
            "--workpath", str(self.project_root / "build"),
            str(self.project_root / "src" / "main.py")
        ]
        
        try:
            subprocess.run(pyinstaller_cmd, check=True)
            print("✅ Aplicación compilada exitosamente")
        except subprocess.CalledProcessError as e:
            print(f"⚠️  Error al compilar la aplicación: {str(e)}")
            raise

    def _move_compiled_app(self):
        """Mueve la aplicación compilada al directorio de paquete"""
        compiled_app = self.build_dir / f"{self.app_name}.app"
        if not compiled_app.exists():
            raise FileNotFoundError(f"No se encontró la aplicación compilada en {compiled_app}")
            
        dest = self.pkg_dir / f"{self.app_name}.app"
        if dest.exists():
            shutil.rmtree(dest)
            
        shutil.move(str(compiled_app), str(self.pkg_dir))
        print(f"📦 Aplicación movida a: {dest}")

    def _create_distribution(self):
        """Crea el paquete de instalación"""
        print("📦 Creando paquete de instalación...")
        
        # Crear scripts de pre/post instalación
        self._create_install_scripts()
        
        # Generar archivo de componentes
        component_plist = self.build_dir / "component.plist"
        self._generate_component_plist(component_plist)
        
        # Comando pkgbuild
        cmd = [
            "pkgbuild",
            "--root", str(self.pkg_dir),
            "--component-plist", str(component_plist),
            "--scripts", str(self.pkg_dir / "scripts"),
            "--identifier", f"com.ps2unpacker.{self.app_name}",
            "--version", self.version,
            "--install-location", "/Applications",
            str(self.build_dir / f"{self.app_name}.pkg")
        ]
        
        try:
            subprocess.run(cmd, check=True)
            print("✅ Paquete creado exitosamente")
        except subprocess.CalledProcessError as e:
            print(f"⚠️  Error al crear el paquete: {str(e)}")
            raise

    def _create_install_scripts(self):
        """Crea scripts de pre/post instalación"""
        scripts_dir = self.pkg_dir / "scripts"
        scripts_dir.mkdir(exist_ok=True)
        
        # Script preinstall
        preinstall = scripts_dir / "preinstall"
        with open(preinstall, "w") as f:
            f.write("""#!/bin/bash
# Previene instalación en volúmenes no soportados
if [ "$(diskutil info / | grep 'File System Personality:' | awk '{print $4}')" != "APFS" ]; then
    osascript -e 'display dialog "PS2Unpacker requiere un volumen con sistema de archivos APFS." buttons {"OK"} default button 1 with icon stop'
    exit 1
fi
""")
        preinstall.chmod(0o755)
        print(f"📜 Script creado: {preinstall}")

        # Script postinstall
        postinstall = scripts_dir / "postinstall"
        with open(postinstall, "w") as f:
            f.write("""#!/bin/bash
# Establecer permisos correctos
chmod -R 755 "/Applications/PS2Unpacker.app"

# Notificar al usuario
osascript <<EOD
display dialog "PS2Unpacker se ha instalado correctamente en su Aplicaciones." ¬
with title "Instalación Completada" ¬
buttons {"OK"} default button 1 ¬
with icon POSIX file "/Applications/PS2Unpacker.app/Contents/Resources/app.icns"
EOD
""")
        postinstall.chmod(0o755)
        print(f"📜 Script creado: {postinstall}")

    def _generate_component_plist(self, output_path):
        """Genera el archivo component.plist"""
        content = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<array>
    <dict>
        <key>BundleHasStrictIdentifier</key>
        <true/>
        <key>BundleIsRelocatable</key>
        <false/>
        <key>BundleIsVersionChecked</key>
        <true/>
        <key>BundleOverwriteAction</key>
        <string>upgrade</string>
        <key>RootRelativeBundlePath</key>
        <string>PS2Unpacker.app</string>
    </dict>
</array>
</plist>"""
        
        with open(output_path, "w") as f:
            f.write(content)
        print(f"📄 Component.plist creado: {output_path}")

    def _sign_package(self):
        """Firma el paquete (requiere identidad de desarrollador)"""
        if not shutil.which("productsign"):
            print("⚠️  'productsign' no encontrado - omitiendo firma")
            return
            
        pkg_path = self.build_dir / f"{self.app_name}.pkg"
        signed_pkg = self.build_dir / f"{self.app_name}-signed.pkg"
        
        try:
            print("🔐 Intentando firmar el paquete...")
            subprocess.run([
                "productsign",
                "--sign", "Developer ID Installer",
                str(pkg_path),
                str(signed_pkg)
            ], check=True)
            
            # Reemplazar el paquete no firmado
            pkg_path.unlink()
            signed_pkg.rename(pkg_path)
            print("✅ Paquete firmado correctamente")
        except subprocess.CalledProcessError as e:
            print(f"⚠️  Error al firmar el paquete: {str(e)}")
        except Exception as e:
            print(f"⚠️  Error inesperado al firmar: {str(e)}")

if __name__ == "__main__":
    try:
        installer = MacOSInstaller()
        installer.build_package()
    except Exception as e:
        print(f"\n❌ Error durante la construcción: {str(e)}")
        exit(1)