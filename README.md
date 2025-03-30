# PS2 Unpacker
# 🎮 PS2 BIOS Unpacker Tool (GUI Edition)

![Banner del Proyecto](src/resources/icons/png/512.png)

> **Herramienta profesional para extraer y analizar BIOS de PlayStation 2**  
> *Versión con interfaz gráfica basada en el trabajo original de [78edu](https://github.com/78edu/playstation2-bios-extract)*
> *Para esto primero debes hacerle un volcado de memoria a tu PS2 Fisica Model_SCPH-XXXXX para obtener el archivo .rom0 usando el programa BiosDrain del usuario [f0bes](https://github.com/F0bes/biosdrain), este mismo archivo sera el que nuestro programa de PS2 Unpacker interprete como desempaquetable en la aplicación.

## 🌟 Características Principales

- **Interfaz gráfica moderna** desarrollada con PyQt5
- **Soporte multiplataforma** (Windows/macOS/Linux)
- Extracción **modular** de componentes de BIOS
- **Preserva la estructura original** de archivos ROM0/BIN
- **Múltiples formatos de salida** (binarios crudos, logs estructurados)
- **Sistema de informes detallados** de extracción
  
## 🛠 Requisitos Técnicos

<div align="center">

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![PyQt5 5.15+](https://img.shields.io/badge/PyQt5-5.15%2B-41CD52?style=for-the-badge&logo=qt&logoColor=white)](https://pypi.org/project/PyQt5/)
[![Platforms](https://img.shields.io/badge/Platforms-Windows%20%7C%20macOS%20%7C%20Linux-999999?style=for-the-badge)](https://github.com/panecitoazucarado/PS2Unpacker/releases)
[![License](https://img.shields.io/badge/License-MIT-A31F34?style=for-the-badge)](LICENSE)

</div>



# 🌟 Características Principales
> ✔ Interfaz gráfica moderna con PyQt5
> ✔ Soporte multiplataforma (Windows/macOS/Linux)
> ✔ Extracción modular de componentes BIOS
> ✔ Preserva estructura original de archivos ROM0/BIN
> ✔ Múltiples formatos de salida (binarios crudos, logs estructurados)
> ✔ Informes detallados de extracción

🚀 Instalación Rápida
📥 Descarga Directa (macOS)
<div align="center"> <a href="https://github.com/panecitoazucarado/PS2Unpacker/releases/latest/download/PS2Unpacker.pkg"> <img src="https://img.shields.io/badge/Download-macOS_Installer-0078d7?style=for-the-badge&logo=apple" alt="Download macOS Installer"/> </a> </div>

# PS2 BIOS Unpacker - Terminal Edition

## INSTALACIÓN
```bash
# 1. Clonar repositorio
gh repo clone panecitoazucarado/PS2Unpacker

# 2. Entrar al directorio
cd PS2Unpacker

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar aplicación
python src/main.py
