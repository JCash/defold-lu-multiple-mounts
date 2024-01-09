#!/usr/bin/env bash

SDK_VERSION=1.6.2
# SDK_ZIP=defoldsdk.zip
# SDK_URL=https://github.com/defold/defold/releases/download/${SDK_VERSION}/${SDK_ZIP}
BOB_JAR=bob.jar
BOB_URL=https://github.com/defold/defold/releases/download/${SDK_VERSION}/${BOB_JAR}

BUILD_FOLDER=./build
SDK_FOLDER=${BUILD_FOLDER}/defoldsdk

mkdir -p ${BUILD_FOLDER}

set -e

# if [ ! -e "${BUILD_FOLDER}/${SDK_ZIP}" ]; then
#     curl -L ${SDK_URL} -o ${BUILD_FOLDER}/${SDK_ZIP}
# fi

# if [ ! -d "${SDK_FOLDER}" ]; then
#     unzip ${BUILD_FOLDER}/defoldsdk.zip "defoldsdk/lib/python/*" "defoldsdk/ext/lib/python/*" -d ${BUILD_FOLDER}
# fi

if [ ! -e "${BUILD_FOLDER}/${BOB_JAR}" ]; then
    curl -L ${BOB_URL} -o ${BUILD_FOLDER}/${BOB_JAR}
fi
