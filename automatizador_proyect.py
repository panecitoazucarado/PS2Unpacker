import os
from pathlib import Path

def create_project_structure(root_path):
    # Directorios principales
    dirs = [
        ".github/workflows",
        "bin",
        "dist",
        "docs",
        "icons/macos",
        "icons/windows",
        "icons/png",
        "packaging/macos",
        "packaging/windows",
        "packaging/linux",
        "src/core",
        "src/gui",
        "src/resources/qss",
        "src/resources/translations",
        "tests/unit",
        "tests/integration"
    ]
    
    # Archivos base
    files = {
        "docs/INSTALL.md": "# Guía de Instalación\n\n...",
        "docs/USER_GUIDE.md": "# Manual de Usuario\n\n...",
        "docs/DEVELOPER.md": "# Documentación para Desarrolladores\n\n...",
        ".gitignore": """# Python
__pycache__/
*.py[cod]
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Entornos virtuales
venv/
ENV/
env/

# Sistema
.DS_Store
Thumbs.db
""",
        "LICENSE": "MIT License\n\nCopyright (c) [year] [fullname]\n...",
        "pyproject.toml": "[build-system]\nrequires = [\"setuptools>=42\"]\nbuild-backend = \"setuptools.build_meta\"",
        "README.md": "# PS2 Unpacker\n\n...",
        "requirements-dev.txt": "pytest\ncoverage\nflake8\nblack\nmypy",
        "requirements.txt": "PyQt5\npython-dateutil\npyinstaller",
        "setup.py": "from setuptools import setup, find_packages\n\nsetup(\n    name='PS2Unpacker',\n    version='0.1.0',\n    packages=find_packages(),\n    install_requires=[\n        'PyQt5',\n        'python-dateutil'\n    ],\n)",
        ".github/workflows/build-mac.yml": "name: Build macOS\n\non: [push, pull_request]\n\njobs:\n  build:\n    runs-on: macos-latest\n    steps:\n      - uses: actions/checkout@v2\n      - name: Set up Python\n        uses: actions/setup-python@v2\n      - name: Install dependencies\n        run: pip install -r requirements.txt\n      - name: Build application\n        run: bash bin/build_mac.sh",
        ".github/workflows/build-win.yml": "name: Build Windows\n\non: [push, pull_request]\n\njobs:\n  build:\n    runs-on: windows-latest\n    steps:\n      - uses: actions/checkout@v2\n      - name: Set up Python\n        uses: actions/setup-python@v2\n      - name: Install dependencies\n        run: pip install -r requirements.txt\n      - name: Build application\n        run: powershell .\\bin\\build_win.ps1",
        ".github/workflows/build-linux.yml": "name: Build Linux\n\non: [push, pull_request]\n\njobs:\n  build:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v2\n      - name: Set up Python\n        uses: actions/setup-python@v2\n      - name: Install dependencies\n        run: pip install -r requirements.txt\n      - name: Build application\n        run: bash bin/build_linux.sh",
        "packaging/macos/Info.plist": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">\n<plist version=\"1.0\">\n<dict>\n    <key>CFBundleName</key>\n    <string>PS2Unpacker</string>\n</dict>\n</plist>",
        "packaging/windows/setup.iss": "[Setup]\nAppName=PS2 Unpacker\nAppVersion=1.0\nDefaultDirName={pf}\\PS2 Unpacker\nOutputDir=dist\nOutputBaseFilename=PS2Unpacker_Setup\n",
        "packaging/linux/ps2-unpacker.desktop": "[Desktop Entry]\nName=PS2 Unpacker\nExec=ps2-unpacker\nIcon=ps2-unpacker\nType=Application\nCategories=Utility;"
    }

    # Crear directorios
    for directory in dirs:
        dir_path = Path(root_path) / directory
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"Directorio creado: {dir_path}")

    # Crear archivos
    for file_path, content in files.items():
        full_path = Path(root_path) / file_path
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Archivo creado: {full_path}")

if __name__ == "__main__":
    project_root = "/Users/heidycolszewski/Desktop/PS2 Unpacker"
    create_project_structure(project_root)
    print("\nEstructura del proyecto creada con éxito!")
    print("Ahora puedes copiar tu código existente a los directorios correspondientes:")
    print(f"- Coloca tu código principal en: {project_root}/src/core")
    print(f"- Los archivos de interfaz gráfica en: {project_root}/src/gui")
    print(f"- Los recursos (iconos, traducciones) en: {project_root}/src/resources")