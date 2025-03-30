import os
import shutil
from pathlib import Path

def organize_icons(resources_path):
    # Definir estructura objetivo
    icon_structure = {
        'macos': {
            'app.icns': None,  # Se generará después
            'iconset': {
                'icon_16x16.png': None,
                'icon_16x16@2x.png': None,
                'icon_32x32.png': None,
                'icon_32x32@2x.png': None,
                'icon_64x64.png': None,
                'icon_64x64@2x.png': None,
                'icon_128x128.png': None,
                'icon_128x128@2x.png': None,
                'icon_256x256.png': None,
                'icon_256x256@2x.png': None,
                'icon_512x512.png': None,
                'icon_512x512@2x.png': None
            }
        },
        'windows': {
            'app.ico': None  # Se generará después
        },
        'png': {
            '16.png': None,
            '32.png': None,
            '64.png': None,
            '128.png': None,
            '256.png': None,
            '512.png': None
        }
    }

    # Crear estructura de directorios
    base_path = Path(resources_path) / 'icons'
    print(f"\n{'='*50}\nOrganizando iconos en: {base_path}\n{'='*50}")

    for platform, contents in icon_structure.items():
        platform_path = base_path / platform
        platform_path.mkdir(parents=True, exist_ok=True)
        print(f"\n► Creando directorio para {platform.upper()} en: {platform_path}")

        if isinstance(contents, dict):
            for item, _ in contents.items():
                if item.endswith('/'):  # Para subdirectorios
                    (platform_path / item).mkdir(exist_ok=True)
                else:
                    # Marcador de archivo
                    (platform_path / item).touch(exist_ok=True)

    # Mapeo de archivos fuente -> destino
    icon_mapping = {
        # macOS
        'icon_16x16.png': 'macos/iconset/icon_16x16.png',
        'icon_16x16@2x.png': 'macos/iconset/icon_16x16@2x.png',
        'icon_32x32.png': 'macos/iconset/icon_32x32.png',
        'icon_32x32@2x.png': 'macos/iconset/icon_32x32@2x.png',
        'icon_64x64.png': 'macos/iconset/icon_64x64.png',
        'icon_64x64@2x.png': 'macos/iconset/icon_64x64@2x.png',
        'icon_128x128.png': 'macos/iconset/icon_128x128.png',
        'icon_128x128@2x.png': 'macos/iconset/icon_128x128@2x.png',
        'icon_256x256.png': 'macos/iconset/icon_256x256.png',
        'icon_256x256@2x.png': 'macos/iconset/icon_256x256@2x.png',
        'icon_512x512.png': 'macos/iconset/icon_512x512.png',
        'icon_512x512@2x.png': 'macos/iconset/icon_512x512@2x.png',
        
        # Windows (se generará después)
        
        # PNG base
        'icon_16x16.png': 'png/16.png',
        'icon_32x32.png': 'png/32.png',
        'icon_64x64.png': 'png/64.png',
        'icon_128x128.png': 'png/128.png',
        'icon_256x256.png': 'png/256.png',
        'icon_512x512.png': 'png/512.png'
    }

    # Mover archivos existentes
    source_dir = Path(resources_path) / 'icons'
    moved_files = set()

    print("\n🔀 Moviendo archivos a la nueva estructura...")
    for old_name, new_path in icon_mapping.items():
        src = source_dir / old_name
        dest = base_path / new_path
        
        if src.exists():
            shutil.move(str(src), str(dest))
            print(f"  ✓ {old_name} -> {new_path}")
            moved_files.add(old_name)
        else:
            print(f"  ✗ {old_name} no encontrado (se esperaba en: {src})")

    # Generar .icns para macOS (requiere iconutil)
    print("\n🛠 Generando archivos compilados...")
    try:
        iconset_dir = base_path / 'macos' / 'iconset'
        icns_file = base_path / 'macos' / 'app.icns'
        
        if iconset_dir.exists():
            os.system(f"iconutil -c icns '{iconset_dir}' -o '{icns_file}'")
            print(f"  ✓ Generado app.icns para macOS")
        else:
            print("  ✗ No se pudo generar app.icns: falta el iconset")
    except Exception as e:
        print(f"  ✗ Error generando .icns: {str(e)}")

    # Generar .ico para Windows (requiere imagemagick)
    try:
        ico_file = base_path / 'windows' / 'app.ico'
        png_files = sorted(base_path.glob('png/*.png'))
        
        if png_files:
            png_list = ' '.join(f'"{p}"' for p in png_files)
            os.system(f"convert {png_list} '{ico_file}'")
            print(f"  ✓ Generado app.ico para Windows")
        else:
            print("  ✗ No se pudo generar .ico: faltan PNG base")
    except Exception as e:
        print(f"  ✗ Error generando .ico: {str(e)}")

    # Limpieza final
    print("\n🧹 Limpiando archivos temporales...")
    for item in source_dir.glob('*'):
        if item.name not in ['macos', 'windows', 'png'] and item.is_file():
            item.unlink()
            print(f"  ✓ Eliminado {item.name}")

    print(f"\n{'='*50}")
    print("✅ Organización completada con éxito!")
    print(f"Iconos disponibles en: {base_path}")
    print("Estructura creada:")
    print("\n".join(f"  • {f}" for f in sorted(base_path.rglob('*'))))
    print("="*50)

if __name__ == "__main__":
    # Ruta a tu directorio resources (ajusta según tu proyecto)
    resources_path = "/Users/heidycolszewski/Desktop/PS2 Unpacker/resources"
    
    if Path(resources_path).exists():
        organize_icons(resources_path)
    else:
        print(f"Error: No se encontró el directorio {resources_path}")
        print("Por favor ajusta la variable 'resources_path' en el script")