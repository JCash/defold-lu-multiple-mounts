# LiveUpdate example with multiple mounts

This example shows how to add and remove multiple mounts.

## Setup

_NOTE:_ Defold cannot currently create multiple archives at build time, so we have to configure this manually at this time.

To generate the .zip files, we use the Protobuf files from our sdk to read/write the manifest files for each archive.

_NOTE:_ We currently need the Defold source downloaded, and the `DYNAMO_HOME` set in order to find the correct *pb2.py files.

The packages themselves are defined in [](./make_packages.py), with a hardcoded list of files that should go into each .zip file.

## Build and test

* Download the bob.jar

    $ ./setup.sh

* Build+bundle the game, using the liveupdate settings.

    $ ./build.sh

* Run the game

    $ ./bundle_new/LiveUpdateMounts.app/Contents/MacOS/LiveUpdateMounts

_Note:_ It generates a big Live Update archive (.zip), which we'll use in this example.
