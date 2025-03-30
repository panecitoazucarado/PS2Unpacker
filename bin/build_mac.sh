#!/bin/bash

# Configuración
APP_NAME="PS2Unpacker"
VERSION="1.0.0"
IDENTIFIER="com.ps2unpacker.app"
RESOURCES_DIR="src/resources"
ICNS_FILE="$RESOURCES_DIR/icons/macos/app.icns"
BUILD_DIR="dist/mac"
PKG_DIR="$BUILD_DIR/pkg"
APP_CONTENTS="$PKG_DIR/$APP_NAME.app/Contents"

# Limpiar build anterior
rm -rf "$BUILD_DIR"
mkdir -p "$APP_CONTENTS/MacOS"
mkdir -p "$APP_CONTENTS/Resources"

# Compilar con PyInstaller (incluyendo recursos)
echo "🔨 Compilando aplicación..."
pyinstaller --noconfirm --windowed --name "$APP_NAME" \
    --icon "$ICNS_FILE" \
    --osx-bundle-identifier "$IDENTIFIER" \
    --add-data "$RESOURCES_DIR/icons:resources/icons" \
    --add-data "$RESOURCES_DIR/qss:resources/qss" \
    --add-data "$RESOURCES_DIR/translations:resources/translations" \
    "src/main.py"

# Mover el .app al directorio de paquete
echo "📦 Preparando paquete..."
mv "dist/$APP_NAME.app" "$APP_CONTENTS/"

# Crear estructura de directorios necesaria
mkdir -p "$APP_CONTENTS/Resources"
mkdir -p "$APP_CONTENTS/Frameworks"
mkdir -p "$APP_CONTENTS/PlugIns"

# Crear Info.plist
cat <<EOF > "$APP_CONTENTS/Info.plist"
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>$APP_NAME</string>
    <key>CFBundleIconFile</key>
    <string>app.icns</string>
    <key>CFBundleIdentifier</key>
    <string>$IDENTIFIER</string>
    <key>CFBundleName</key>
    <string>$APP_NAME</string>
    <key>CFBundleVersion</key>
    <string>$VERSION</string>
    <key>CFBundleShortVersionString</key>
    <string>$VERSION</string>
    <key>NSHighResolutionCapable</key>
    <true/>
    <key>LSUIElement</key>
    <false/>
</dict>
</plist>
EOF

# Copiar icono
cp "$ICNS_FILE" "$APP_CONTENTS/Resources/"

echo "✅ Aplicación compilada en: $BUILD_DIR"