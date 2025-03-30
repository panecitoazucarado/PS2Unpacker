# PS2 Unpacker
# 🎮 PS2 BIOS Unpacker Tool (GUI Edition)

<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="src/resources/icons/png/512.png" alt="Icono de la aplicación" width="200"/>
        <br>
        <em>Icono de PS2Unpacker</em>
      </td>
      <td align="center">
        <img src="https://github.com/panecitoazucarado/PS2Unpacker/blob/main/banners/Logo.png" alt="Logo de PS2Unpacker" width="200"/>
        <br>
        <em>Logo del proyecto</em>
      </td>
    </tr>
  </table>
</div>

> **Herramienta profesional para extraer y analizar BIOS de PlayStation 2**  
> *Versión con interfaz gráfica basada en el trabajo original de [78edu](https://github.com/78edu/playstation2-bios-extract)*
> 
> *Para esto primero debes hacerle un volcado de memoria a tu PS2 Fisica Model_SCPH-XXXXX para obtener el archivo .rom0 usando el programa BiosDrain del usuario [f0bes](https://github.com/F0bes/biosdrain), este mismo archivo sera el que nuestro programa de PS2 Unpacker interprete como desempaquetable en la aplicación.*

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

## 🍎 Tutorial de Uso en macOS

<div align="center">
  <table>
    <!-- Paso 1 -->
    <tr>
      <td align="center" width="50%">
        <img src="https://github.com/panecitoazucarado/PS2Unpacker/blob/main/Tutorial%20uso%20de%20la%20App%20-Secuencia%20de%20Pasos/Mac%20OS/paso%201.png" alt="Paso 1" width="300"/>
      </td>
      <td width="50%">
        <h3>Paso 1: Inicio - Finalizada la instalacion en Mac OS</h3>
        <p>🔹 <em>Una vez finalizada la instalación, tendrás una interfaz elegante y sencilla, fácil de usar y sin complicaciones. Deberás buscar la ROM extraída de tu PS2 utilizando el programa BiosDrain de [f0bes](https://github.com/F0bes/biosdrain) en tu consola PS2. Luego, importa el archivo .rom0. También puedes cambiar su extensión a .bin, y el programa lo reconocerá sin problemas.</em></p>
      </td>
    </tr>
    <!-- Paso 2 -->
    <tr>
      <td align="center">
        <img src="https://github.com/panecitoazucarado/PS2Unpacker/blob/main/Tutorial%20uso%20de%20la%20App%20-Secuencia%20de%20Pasos/Mac%20OS/paso%202%20mi%20carpeta%20con%20mi%20bios%20de%20mi%20consola%20super%20slim.png" alt="Paso 2" width="300"/>
      </td>
      <td>
        <h3>Paso 2: Selección de archivos</h3>
        <p>🔹 <em>Una vez que hayas realizado la extracción utilizando BiosDrain.elf, el programa generará varios archivos en tu USB. De estos archivos, debes seleccionar el que tenga la extensión .rom0 y cargarlo en el programa. Para hacerlo, simplemente ábrelo utilizando la opción “Open” (Abrir).</em></p>
      </td>
    </tr>
    <!-- Paso 3 -->
    <tr>
      <td align="center">
        <img src="https://github.com/panecitoazucarado/PS2Unpacker/blob/main/Tutorial%20uso%20de%20la%20App%20-Secuencia%20de%20Pasos/Mac%20OS/paso%203.png" alt="Paso 3" width="300"/>
      </td>
      <td>
        <h3>Paso 3: Procesamiento</h3>
        <p>🔹 <em>El programa procesará el contenido del archivo .rom0 y mostrará su contenido en la interfaz. Desde ahí, el usuario podrá seleccionar qué archivos desea exportar a su carpeta de Descargas.

Al desempaquetar los archivos, se creará automáticamente una carpeta llamada “extraction_bios”, donde se almacenará todo el contenido extraído.

El usuario tiene dos opciones:
	1.	Extraer todos los archivos: La BIOS en formato .rom0 suele ocupar entre 4.2 MB y 4.7 MB.
	2.	Extraer archivos de forma individual: Permite seleccionar y extraer únicamente los archivos necesarios.

La decisión dependerá de cómo el usuario desee trabajar con los archivos extraídos.</em></p>
      </td>
    </tr>
    <!-- Paso 4 -->
    <tr>
      <td align="center">
        <img src="https://github.com/panecitoazucarado/PS2Unpacker/blob/main/Tutorial%20uso%20de%20la%20App%20-Secuencia%20de%20Pasos/Mac%20OS/paso%204.png" alt="Paso 4" width="300"/>
      </td>
      <td>
        <h3>Paso 4: Confirmación</h3>
        <p>🔹 <em>Indica qué debe verificar el usuario antes de continuar.</em></p>
      </td>
    </tr>
    <!-- Paso 5 -->
    <tr>
      <td align="center">
        <img src="https://github.com/panecitoazucarado/PS2Unpacker/blob/main/Tutorial%20uso%20de%20la%20App%20-Secuencia%20de%20Pasos/Mac%20OS/paso%205.png" alt="Paso 5" width="300"/>
      </td>
      <td>
        <h3>Paso 5: Extracción</h3>
        <p>🔹 <em>Detalla cómo se completan las operaciones con los archivos.</em></p>
      </td>
    </tr>
    <!-- Paso 6 -->
    <tr>
      <td align="center">
        <img src="https://github.com/panecitoazucarado/PS2Unpacker/blob/main/Tutorial%20uso%20de%20la%20App%20-Secuencia%20de%20Pasos/Mac%20OS/paso%206%20final.png" alt="Paso 6" width="300"/>
      </td>
      <td>
        <h3>Paso 6: Finalización</h3>
        <p>🔹 <em>Explica qué hacer al terminar (ej: ubicación de los archivos resultantes).</em></p>
      </td>
    </tr>
  </table>
</div>

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
