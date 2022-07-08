#!/bin/bash

cd "$(dirname "$0")" || exit

ALTSERVER_VERSION="v0.0.4"
ALTSTORE_VERSION="1_5"

if [ ! -f "./resources/AltServer" ]; then
    curl -L "https://github.com/NyaMisty/AltServer-Linux/releases/download/$ALTSERVER_VERSION/AltServer-x86_64" > "./resources/AltServer"
fi
if [ ! -f "./resources/AltStore.ipa" ]; then
    curl -L "https://cdn.altstore.io/file/altstore/apps/altstore/$ALTSTORE_VERSION.ipa" > "./resources/AltStore.ipa"
fi
if [ -d "./AltLinux/usr/lib" ]; then
    rm -rf "./AltServer/usr/lib"
fi
if [ -d "./dist" ]; then
    rm -rf "./dist"
fi

chmod -R 0775 AltLinux
pyinstaller -w -n altlinux main.py --clean
cp -R ./resources ./dist/altlinux
if [ ! -d "./AltLinux/usr/lib" ]; then
    mkdir "./AltLinux/usr/lib"
fi

cp -R ./dist/altlinux ./AltLinux/usr/lib
dpkg-deb --build --root-owner-group AltLinux AltLinux.deb
