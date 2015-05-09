The Tessel Camera component allows the remote triggering of a photo via a WAMP procedure call. The photo is returned as the call result. (Since the Tessel is very slow in processing and transferring the image, this uses progressive call result to inform you of what step is currently taking place).

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

This also serves a frontend where you can view the accelerometer data logged at

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

Then run `camera.js` on a Tessel with an accelerometer module connected to port A.

```shell
tessel run camera.js
```

This should log

```

```

Once this is running, in the browser frontend click on `take photo`. You should first see the progress report indicators, e.g. `XXXXXX` and the, eventually, the photo.

## The API

The component exposes a single procedure

```
io.crossbar.examples.tessel.camera.take_photo
```

This returns a hex-encoded photo.

The procedure can also be called to yield [progressive results](../docs/Progressive Call Results) by setting the option `receive_progress: true`. In this case, a third handler is attached to the call, and this receives updates about the stage of the process (e.g. "photo taken", "transmitting photo").

## Using it

In your own project:

* Set the `require_websocket_subprotocol` option on your WebSocket transport in the Crossbar.io config. The Tessel WebSocket library does not correctly negotiate this.
* Install the npm libraries `wamp-tessel` and `camera-vc0706`. 
* Adapt the procedure URL for taking a photo to your own needs.