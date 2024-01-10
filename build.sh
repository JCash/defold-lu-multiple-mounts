#!/usr/bin/env bash

PLATFORM=x86_64-macos
BUILDDIR=./build
BUNDLEDIR=./bundle_new
ZIPDIR=${BUILDDIR}/big_lu_archive

mkdir -p ${ZIPDIR}
# The zip-filepath specified in the liveupdate.settings
ZIPDIR=$(realpath ${ZIPDIR})

echo "[test]" > ${BUILDDIR}/test.ini
echo "resource_dir = ${ZIPDIR}" >> ${BUILDDIR}/test.ini
echo "enabled = 1" >> ${BUILDDIR}/test.ini

java -jar ./bob.jar resolve
java -jar ${BUILDDIR}/bob.jar --settings=${BUILDDIR}/test.ini --platform=${PLATFORM} --architectures=${PLATFORM} --variant=debug clean build --archive --liveupdate yes bundle -bo ${BUNDLEDIR}

# rename all files in the export folder to the common name
for name in ${ZIPDIR}/*.zip; do
    mv -v ${name} ${ZIPDIR}/liveupdate.zip
done

echo "CUSTOM FILE DATA" > custom.txt
zip ${ZIPDIR}/liveupdate.zip custom.txt
rm custom.txt
