# LiveUpdate example with a single mount

This example shows how to add and remove a mount using `liveupdate.add_mount()` and `liveupdate.remove_mount()`.

## Build and test

* Download the bob.jar

    $ ./setup.sh

* Build+bundle the game, using the liveupdate settings.

    $ ./build.sh

* Run the game

    $ ./bundle_new/LiveUpdateMounts.app/Contents/MacOS/LiveUpdateMounts

_Note:_ It generates a big Live Update archive (.zip), which we'll use in this example.
