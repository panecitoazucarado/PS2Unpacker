# Carpeta `dist` - Explicación

La carpeta `dist` (abreviatura de "distribution") contiene los archivos listos para la distribución de la aplicación. Es una parte importante del proceso de empaquetado de tu proyecto, ya que es donde se generan los archivos que finalmente serán utilizados por los usuarios finales para ejecutar el programa. Aquí se encuentra todo lo necesario para que el software se ejecute sin necesidad de configuraciones adicionales.

### ¿Qué debe contener la carpeta `dist`?

Dentro de la carpeta `dist`, deberías encontrar lo siguiente:

1. **Archivos ejecutables**:
   - Dependiendo del sistema operativo, deberías tener los ejecutables empaquetados, como un `.exe` para Windows, un `.app` para macOS o archivos compatibles para otros sistemas.
   - Ejemplo: `PS2Unpacker_Windows.exe` para Windows, `PS2Unpacker.app` para macOS.

2. **Archivos de iconos**:
   - Los iconos deben estar incluidos para que la aplicación pueda ser visualizada correctamente en la barra de tareas o en el dock, según el sistema operativo. Esto mejora la apariencia y la usabilidad del programa.
   - Ejemplo: `icon_512x512@2x.ico` o `icon.png`.

3. **Archivos de dependencias**:
   - En algunos casos, las dependencias necesarias para que la aplicación funcione correctamente (por ejemplo, bibliotecas o archivos `.dll` en Windows) también deben estar dentro de esta carpeta. Asegúrate de incluir cualquier archivo de soporte necesario.

4. **Archivos de configuración**:
   - Si el programa utiliza configuraciones predefinidas o archivos de configuración específicos para el sistema de ejecución, deben estar aquí también.
   - Ejemplo: archivos `.config` o `.json` que el software use para almacenar configuraciones de usuario.

5. **Otros archivos necesarios**:
   - Cualquier otro archivo o recurso necesario para el funcionamiento del programa debe ser incluido en la carpeta `dist`. Esto puede incluir documentación adicional, imágenes o cualquier otro archivo auxiliar que el programa necesite para ejecutarse correctamente.

### ¿Por qué es importante esta carpeta?

La carpeta `dist` facilita la distribución de la aplicación sin tener que preocuparse por los detalles técnicos de cómo empaquetar el código fuente o las dependencias. Al proporcionar todo lo necesario en esta carpeta, puedes compartir fácilmente tu aplicación con los usuarios finales de manera rápida y eficiente.

### ¿Cómo se genera la carpeta `dist`?

Dependiendo del proceso de construcción de tu proyecto, la carpeta `dist` puede generarse automáticamente a través de un script de construcción, como **PyInstaller** o **cx_Freeze** para Python, o mediante herramientas específicas del entorno de desarrollo como **Electron** o **npm** para aplicaciones web.

Por ejemplo, si estás utilizando **PyInstaller** para empaquetar tu proyecto en un ejecutable, la carpeta `dist` se generará automáticamente al ejecutar el siguiente comando:

```bash
pyinstaller --onefile your_script.py
