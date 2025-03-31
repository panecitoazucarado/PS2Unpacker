Documentación del Script de Creación de Instalador para macOS
📝 create_installer_mac.py
Este script automatiza la creación de un instalador .pkg para macOS de la aplicación PS2Unpacker. El paquete resultante puede ser distribuido e instalado fácilmente en sistemas macOS.

🏗️ ¿Qué hace exactamente?
Prepara la estructura de directorios necesaria para construir el instalador

Compila la aplicación usando PyInstaller (convirtiendo el código Python en una app nativa de macOS)

Empaqueta la aplicación en un instalador .pkg profesional

Incluye scripts de pre/post instalación para mejorar la experiencia del usuario

Opcionalmente firma el paquete para distribución oficial (requiere certificado de desarrollador Apple)

🛠️ Componentes principales
1. Configuración inicial (__init__)
Define rutas importantes (directorio raíz, carpeta de construcción)

Establece nombre de la aplicación y versión

2. Construcción del paquete (build_package)
Orquesta todo el proceso de construcción en 5 pasos ordenados

3. Preparación de directorios (_prepare_directories)
Crea la estructura de carpetas necesaria:

/dist/mac - Resultados finales

/dist/mac/pkg - Archivos temporales para el paquete

Estructura de la aplicación (.app)

4. Compilación con PyInstaller (_build_app)
Convierte el código Python en una aplicación macOS nativa

Incluye todos los recursos (iconos, traducciones, estilos)

Genera un archivo .app autónomo

5. Movimiento de la aplicación compilada (_move_compiled_app)
Toma la aplicación generada y la coloca en la ubicación correcta para el empaquetado

6. Creación del instalador (_create_distribution)
Usa pkgbuild (herramienta nativa de macOS) para crear el paquete de instalación

Incluye:

Scripts de pre-instalación (verifica requisitos)

Scripts de post-instalación (notifica al usuario)

Metadatos del paquete

7. Scripts de instalación (_create_install_scripts)
Preinstall: Verifica que el sistema tenga APFS (requisito)

Postinstall: Muestra notificación de éxito y ajusta permisos

8. Firma del paquete (_sign_package)
Opcional: Firma el paquete con identidad de desarrollador Apple para distribución oficial

🚀 ¿Por qué es necesario?
Distribución profesional: Crea instaladores estándar de macOS que los usuarios conocen

Facilidad de uso: Permite instalar con doble clic como cualquier otra app

Integración completa: La aplicación aparece en la carpeta Aplicaciones y funciona como nativa

Verificación de requisitos: Asegura que el sistema cumple con los requerimientos

Experiencia de usuario: Proporciona retroalimentación visual durante la instalación

📦 Estructura del paquete final
PS2Unpacker.pkg

├── PS2Unpacker.app
│   ├── Contents
│   │   ├── MacOS/ (ejecutable principal)
│   │   └── Resources/ (iconos, traducciones, estilos)
└── scripts/
    ├── preinstall (verificaciones previas)
    └── postinstall (acciones posteriores)

🔧 Requisitos para usar este script
macOS (versión reciente)

Python 3.x instalado

PyInstaller (pip install pyinstaller)

(Opcional) Certificado de desarrollador Apple para firmar

▶️ Cómo usarlo
Colocar este script en la raíz del proyecto

Ejecutar con Python 3:

python3 create_installer_mac.py

El instalador estará en dist/mac/PS2Unpacker.pkg

ℹ️ Notas importantes
El script está diseñado para el proyecto PS2Unpacker específicamente

Las rutas a los recursos asumen una estructura particular del proyecto

La firma del paquete es opcional pero recomendada para distribución pública

Los scripts de instalación pueden personalizarse según necesidades específicas

Este instalador proporciona una forma profesional y confiable de distribuir la aplicación PS2Unpacker a usuarios de macOS, garantizando una experiencia de instalación sencilla y familiar.