# LiveUpdate example with multiple mounts

This example shows how to add and remove multiple mounts.

## Setup

_NOTE:_ Defold cannot currently create multiple archives at build time, so we have to configure this manually at this time.

To generate the .zip files, we use the Protobuf files from our sdk to read/write the manifest files for each archive.

The packages themselves are defined in [](./make_packages.py), with a hardcoded list of files that should go into each .zip file.

## Build

* Download the python files from the sdk

    $ ./setup.sh

* Build the game, using the liveupdate settings.

    $ ./build.sh

_Note:_ It generates a big Live Update archive (.zip), which we won't use in this example.
However, we'll use the base game archive.

_Note:_ It also calls ./make_packages.py, to manually create a few .zip files, with corresponding .dmanifest files.
