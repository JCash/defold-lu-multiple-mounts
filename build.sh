#!/usr/bin/env bash

PLATFORM=x86_64-macos
BUILDDIR=./build
BUNDLEDIR=./bundle_new
ZIPDIR=${BUILDDIR}/big_lu_archive
BOB_JAR=${BUILDDIR}/bob.jar

mkdir -p ${ZIPDIR}
# The zip-filepath specified in the liveupdate.settings
ZIPDIR=$(realpath ${ZIPDIR})

echo "[test]" > ${BUILDDIR}/test.ini
echo "resource_dir = ${ZIPDIR}" >> ${BUILDDIR}/test.ini
echo "enabled = 1" >> ${BUILDDIR}/test.ini

java -jar ${BOB_JAR} resolve
java -jar ${BOB_JAR} --settings=${BUILDDIR}/test.ini --platform=${PLATFORM} --architectures=${PLATFORM} --variant=debug clean build --archive --liveupdate yes bundle -bo ${BUNDLEDIR}

VERSION=$(java -jar ${BOB_JAR} --version)
BOB_VERSION=$(echo ${VERSION} | awk -F' ' '{print $3}')
BUILD_DATE=$(date)

# rename all files in the export folder to the common name
for name in ${ZIPDIR}/*.zip; do
    mv -v ${name} ${ZIPDIR}/liveupdate.zip
done

echo "CUSTOM FILE DATA" > custom.txt
echo "{\"version\": \"${BOB_VERSION}\", \"date\": \"${BUILD_DATE}\"}" > version_liveupdate.json
cat version_liveupdate.json
zip ${ZIPDIR}/liveupdate.zip custom.txt version_liveupdate.json
rm custom.txt version_liveupdate.json
