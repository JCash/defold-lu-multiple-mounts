# LiveUpdate example with a single mount

This example shows how to add and remove a mount using `liveupdate.add_mount()` and `liveupdate.remove_mount()`.

## Build and test

Download the bob.jar

    $ ./setup.sh

Build+bundle the game, using the liveupdate settings.

    $ ./build.sh

_Note:_ It generates a big Live Update archive (.zip), which we'll use in this example.

## Run the game

Option 1: Loading directly from disc

    $ ./bundle_new/LiveUpdateMounts.app/Contents/MacOS/LiveUpdateMounts

Option 2: Downloading via HTTP

* Start a local http server (default port 8000):

        $ (cd build/big_lu_archive && python -m http.server)

* Boot the game

        $ ./bundle_new/LiveUpdateMounts.app/Contents/MacOS/LiveUpdateMounts --config=test.http_url=http://localhost:8000
