import os
import shutil
from pathlib import Path

class ProjectCleaner:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.required_dirs = {
            'src': [
                'core',
                'gui',
                'resources/icons',
                'resources/qss',
                'resources/translations'
            ],
            'tests': [
                'unit',
                'integration'
            ],
            'docs': [],
            'packaging': [
                'macos',
                'windows',
                'linux'
            ]
        }
        
        self.essential_files = [
            'README.md',
            'LICENSE',
            'pyproject.toml',
            'requirements.txt',
            'requirements-dev.txt',
            '.gitignore',
            'src/main.py'
        ]

    def clean_project(self):
        print(f"🔍 Analizando proyecto en: {self.project_root}")
        self.remove_unnecessary_files()
        self.organize_icons()
        self.verify_structure()
        print("\n✅ Limpieza completada con éxito!")

    def remove_unnecessary_files(self):
        """Elimina archivos innecesarios como .DS_Store y duplicados"""
        print("\n🧹 Eliminando archivos innecesarios...")
        
        # Archivos a eliminar
        unnecessary = [
            '**/.DS_Store',
            '**/desktop.ini',
            '**/Thumbs.db',
            '**/.~lock.*',
            '**/*.bak',
            '**/__pycache__',
            '**/*.pyc',
            '**/*.pyo',
            '**/*.pyd',
            'scripts/iconos/',  # Moveremos estos iconos
            'src/icon.iconset/'  # Iconos duplicados
        ]
        
        for pattern in unnecessary:
            for filepath in self.project_root.glob(pattern):
                if filepath.is_file():
                    filepath.unlink()
                    print(f"  ✓ Eliminado archivo: {filepath}")
                elif filepath.is_dir():
                    shutil.rmtree(filepath)
                    print(f"  ✓ Eliminado directorio: {filepath}")

    def organize_icons(self):
        """Reorganiza los recursos de iconos en src/resources/icons"""
        print("\n🎨 Optimizando estructura de iconos...")
        
        # Directorio destino principal (usando tu estructura actual)
        icons_dir = self.project_root / 'src' / 'resources' / 'icons'
        icons_dir.mkdir(parents=True, exist_ok=True)
        
        # Fuentes posibles de iconos
        possible_sources = [
            self.project_root / 'scripts' / 'iconos',
            self.project_root / 'src' / 'icon.iconset'
        ]
        
        # Mover todos los iconos a src/resources/icons
        for source in possible_sources:
            if source.exists():
                for item in source.iterdir():
                    if item.name not in ['.DS_Store', 'desktop.ini']:
                        dest = icons_dir / item.name
                        if not dest.exists():
                            shutil.move(str(item), str(icons_dir))
                            print(f"  ✓ Movido: {item} -> {dest}")
                        else:
                            print(f"  ✗ Saltado (ya existe): {item.name}")

        # Crear subdirectorios para plataformas
        platforms = {
            'macos': ['app.icns'],
            'windows': ['app.ico'],
            'png': ['16.png', '32.png', '64.png', '128.png', '256.png', '512.png']
        }
        
        for platform, files in platforms.items():
            platform_dir = icons_dir / platform
            platform_dir.mkdir(exist_ok=True)
            
            for file in files:
                (platform_dir / file).touch(exist_ok=True)

    def verify_structure(self):
        """Verifica y crea estructura esencial faltante"""
        print("\n📁 Verificando estructura del proyecto...")
        
        for main_dir, subdirs in self.required_dirs.items():
            dir_path = self.project_root / main_dir
            dir_path.mkdir(exist_ok=True)
            
            for subdir in subdirs:
                subdir_path = dir_path / subdir
                subdir_path.mkdir(parents=True, exist_ok=True)
                print(f"  ✓ Verificado: {subdir_path}")
        
        for file in self.essential_files:
            file_path = self.project_root / file
            if not file_path.exists():
                file_path.touch()
                print(f"  ✗ Creado archivo faltante: {file_path}")

    def generate_cleanup_report(self):
        """Genera un reporte de cambios recomendados"""
        report = []
        
        # Verificar archivos de construcción
        build_tools = {
            'pyproject.toml': "Recomendado para manejo moderno de paquetes",
            'setup.py': "Puede ser reemplazado por pyproject.toml"
        }
        
        for tool, note in build_tools.items():
            path = self.project_root / tool
            report.append(f"• {tool}: {'✅ Existe' if path.exists() else '❌ Faltante'} - {note}")
        
        return "\n".join(report)

if __name__ == "__main__":
    project_path = "/Users/heidycolszewski/Desktop/PS2 Unpacker"
    cleaner = ProjectCleaner(project_path)
    
    print("="*60)
    print("🛠 PS2 Unpacker - Optimizador de Estructura de Proyecto")
    print("="*60)
    
    cleaner.clean_project()
    
    print("\n📝 Reporte Final:")
    print(cleaner.generate_cleanup_report())
    print("\n💡 Recomendaciones adicionales:")
    print("- Consolidar todos los iconos en 'src/resources/icons/'")
    print("- Usar subdirectorios 'macos', 'windows' y 'png' para iconos")
    print("- Eliminar archivos temporales antes de commits")
    print("="*60)