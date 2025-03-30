# PS2 Unpacker
# 🎮 PS2 BIOS Unpacker Tool (GUI Edition)

![Banner del Proyecto](src/resources/icons/png/512.png)

> **Herramienta profesional para extraer y analizar BIOS de PlayStation 2**  
> *Versión con interfaz gráfica basada en el trabajo original de [78edu](https://github.com/78edu/playstation2-bios-extract)*

## 🌟 Características Principales

- **Interfaz gráfica moderna** desarrollada con PyQt5
- **Soporte multiplataforma** (Windows/macOS/Linux)
- Extracción **modular** de componentes de BIOS
- **Preserva la estructura original** de archivos ROM0/BIN
- **Múltiples formatos de salida** (binarios crudos, logs estructurados)
- **Sistema de informes detallados** de extracción

## 📦 Requisitos del Sistema

```bash
Python 3.8+
PyQt5 5.15+

🚀 Instalación
Método 1: Instalador para macOS

# Descarga el paquete .pkg más reciente (MAC OS)

[**🔽 Descargar última versión (PS2Unpacker.pkg)**](https://github.com/panecitoazucarado/PS2Unpacker/releases/latest/download/PS2Unpacker.pkg)

# Clonar el repositorio

Para clonar este repositorio, simplemente copia y pega el siguiente comando en tu terminal:
git clone https://github.com/panecitoazucarado/PS2Unpacker.git

cd ps2-bios-unpacker
pip install -r requirements.txt
python src/main.py

🛠️ Uso Básico
Seleccionar archivo BIOS (ROM0 o BIN)

Explorar módulos detectados en la lista interactiva

Extraer componentes individuales o toda la BIOS

Revisar los archivos extraídos en ~/Downloads/extraction_bios/

Captura de pantalla
🔍 Tecnologías Utilizadas
Componente	Función
PyQt5	Interfaz gráfica profesional
Python 3.11	Lógica de extracción y procesamiento
PyInstaller	Empacado multiplataforma
GitHub Actions	CI/CD automatizado
🧠 Base Técnica
Este proyecto extiende el trabajo original de 78edu añadiendo:

Sistema de detección mejorado de estructuras ROMDIR

Algoritmo optimizado para lectura de módulos

Manejo de errores robusto con notificaciones al usuario

Soporte para high-DPI (pantallas Retina)

🧩 Estructura del Proyecto

ps2-bios-unpacker/
├── src/                  # Código fuente principal
│   ├── core/             # Lógica de extracción de BIOS
│   ├── gui/              # Componentes de interfaz gráfica
│   └── resources/        # Assets gráficos y traducciones
├── dist/                 # Binarios compilados
├── docs/                 # Documentación técnica
└── packaging/            # Configuraciones de empaquetado

🎨 Personalización
Edita los archivos QSS en src/resources/qss/ para cambiar el tema visual:

/* Ejemplo de tema oscuro */
QWidget {
    background-color: #2d2d2d;
    color: #f0f0f0;
}

🤝 Contribución
Haz fork del proyecto

Crea una rama (git checkout -b feature/awesome-feature)

Haz commit de tus cambios (git commit -m 'Add awesome feature')

Haz push a la rama (git push origin feature/awesome-feature)

Abre un Pull Request

📜 Licencia
Este proyecto está licenciado bajo GPL-3.0 - ver LICENSE para más detalles.

🌍 Comunidad PS2
¡Únete a la conversación!

...
