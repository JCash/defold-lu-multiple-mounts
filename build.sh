#!/usr/bin/env bash

PLATFORM=x86_64-macos
BUILDDIR=./build
BUNDLEDIR=./bundle_new

ZIPDIR=$(realpath ${BUILDDIR}/zips)

echo "[test]" > ${BUILDDIR}/test.ini
echo "resource_dir = ${ZIPDIR}" >> ${BUILDDIR}/test.ini

#java -jar ./bob.jar resolve
java -jar ${BUILDDIR}/bob.jar --settings=${BUILDDIR}/test.ini --platform=${PLATFORM} --architectures=${PLATFORM} --variant=debug clean build --archive --liveupdate yes bundle -bo ${BUNDLEDIR}

DMANIFEST=${BUNDLEDIR}/LiveUpdateMultipleArchives.app/Contents/Resources/game.dmanifest
mkdir -p ./build/tmp
mkdir -p ./build/zips

python ./make_packages.py ${DMANIFEST}
