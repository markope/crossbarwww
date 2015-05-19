The Tessel Accelerometer component publishes the raw accelerometer data from an accelerometer module via WAMP.

## Trying it out

The code for this can be found in the [crossbarexamples GitHub repository](https://github.com/crossbario/crossbarexamples) under `iotcookbook`. You need to clone this (or [download it as a ZIP file](https://github.com/crossbario/crossbarexamples/archive/master.zip)).

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

In `accelerometer.js`, add the URL of the machine on which Crossbar.io runs:

```javascript
var connection = new autobahn.Connection({
   url: "ws://<URL OF YOUR CROSSBAR INSTANCE>/ws", // replace with the url of your crossbar instance
   realm: "iot_cookbook"
});
```

Then run `accelerometer.js` on a Tessel with an accelerometer module connected to port A.

```shell
tessel run accelerometer.js
```

This should log

```shell
accelerometer initialized (output rates: 800,400,200,100,50,12.5,6.25,1.56)
connected!
sending accel data
sending accel data
sending accel data
```

Once this is running, open the browser console for the frontend page, and you'll see the raw accelerometer data logged as it is received.

```shell
received accelerometer data
Object {y: "-0.03", x: "0.02", z: "1.02"}
```

## The API

The accelerometer component publishes the raw accelerometer data as JSON to the topic

```
io.crossbar.examples.tessel.accelerometer.on_accelerometer_data
```

## Using it

In your own project:

* Set the `require_websocket_subprotocol` option on your WebSocket transport in the Crossbar.io config. The Tessel WebSocket library does not correctly negotiate this.
* Install the npm libraries `wamp-tessel` and `accel-mma84`. 
* Adapt the topic which is sent by `accelerometer.js` to your own needs.