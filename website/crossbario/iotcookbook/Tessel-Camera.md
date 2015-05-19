The Tessel Camera component allows the remote triggering of a photo via a WAMP procedure call. The photo is returned as the call result. (Since the Tessel is very slow in processing and transferring the image, you can use progressive call results to inform you of what step is currently taking place).

## Trying it out

Open a shell for the component directory. 

Install the Node.js dependencies by doing

```shell
npm install
```

Start up Crossbar.io:

```shell
crossbar start
```

This also serves a frontend which allows you to trigger the taking of an image and displays the progress feedback as well as the image:

```
http://localhost:8080
```

In `camera.js`, add the URL of the machine on which Crossbar.io runs:

```javascript
var connection = new autobahn.Connection({
   url: "ws://<URL OF YOUR CROSSBAR INSTANCE>/ws", // replace with the url of your crossbar instance
   realm: "iot_cookbook"
});
```

Then run `camera.js` on a Tessel with a camera module connected to port A. (This needs to be port A - no changing ports on this module!)

```shell
tessel run camera.js
```

This should log

```shell
camera ready
main called
connected
Procedure 'io.crossbar.examples.tessel.camera.take_photo' registered: R1993040553
```

You might also get 

```shell
camera error Error: No UART Response...
```

as part of this. This doesn't necessarily mean that the camera is non-functional - just give it a try!

Once this is running, in the browser frontend click on `take photo`. You should first see the progress report indicators, e.g. `Photo has been taken.` and then, eventually, the photo.

## The API

The component exposes a single procedure

```
io.crossbar.examples.tessel.camera.take_photo
```

This returns a hex-encoded photo. (In the example frontent, this is converted to a base64-encoded data URL.)

The procedure can also be called to yield [progressive results](../docs/Progressive Call Results) by setting the option `receive_progress: true`. In this case, a third handler is attached to the call, and this receives updates about the stage of the process (e.g. "photo taken", "transmitting photo"). The provided example uses progressive results.

## Using it

In your own project:

* Set the `require_websocket_subprotocol` option on your WebSocket transport in the Crossbar.io config. The Tessel WebSocket library does not correctly negotiate this.
* Install the npm libraries `wamp-tessel` and `camera-vc0706`. 
* Adapt the procedure URL for taking a photo to your own needs.