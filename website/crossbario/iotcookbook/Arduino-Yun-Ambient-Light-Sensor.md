The Arduino Yun Ambient Light Sensor component allows querying the current state of a Tinkerkit ambient light (LDR) sensor and publishes events when this state changes.

<div class="topimage_container">
   <img class="topimage" src="../../static/img/iotcookbook/yun_ambient_light.jpg" alt="">   
</div>

## Trying it out

The code for this can be found in the [crossbarexamples GitHub repository](https://github.com/crossbario/crossbarexamples) under `iotcookbook`. You need to clone this (or [download it as a ZIP file](https://github.com/crossbario/crossbarexamples/archive/master.zip)).

You need to have one Tinkerkit ambient light (LDR) sensor connected to 'I0' on the Tinkerkit shield (pin 0).

Open a shell for the component directory. 

Start up Crossbar.io:

```shell
crossbar start
```

This also serves a frontend where you can view the ambient light sensor data logged at

```
http://localhost:8080
```

In `ambientlight_yun.js`, add the URL of the machine on which Crossbar.io runs:

```javascript
var connection = new autobahn.Connection({
   url: "ws://<URL OF YOUR CROSSBAR INSTANCE>/ws", // replace with the url of your crossbar instance
   realm: "iot_cookbook"
});
```

You need to set up the Yun for [using AutobahnJS](Arduino Yun AutobahnJS Setup).

Transfer `ambientlight_yun.js` on the Yun, e.g. by doing 

```console
scp ambientlight_yun.js root@<IP of your Yun>:~/
```

The script is run using Node.js, so you need to have this installed ('opkg install node').

Then run `ambientlight_yun.js` 

```shell
node ambientlight_yun.js
```

This should log

```
Arduino Yun Ambientlight Sensor starting ...
Arduino connected (over /dev/ttyATH0, board version 2.3)
Connecting to router ...
Router connected. Session ID: 1595783623
```

Once this is running, open the browser console for the frontend page and reload the page. You shoud see 

```
connected
light level currently is:  73
```

and when you change the lighting conditions

```
Light level changed to:  58
Light level changed to:  56
Light level changed to:  58
Light level changed to:  60
```

## The API

The component provides two procedures

* `io.crossbar.examples.yun.ambientlight.get_light_level` - Returns the current light level as a value between 0 and 100
* `io.crossbar.examples.yun.ambientlight.set_threshold` - Sets the threshold value which needs to be crossed in order to produce events. Takes an integer between 0 and 100.

and publishes to two topics:

* `io.crossbar.examples.yun.ambientlight.on_light_level_change` - Current light level as a value between 0 and 100. Published to if threshold is set to '0'.
* `io.crossbar.examples.yun.ambientlight.on_threshold_passed` - Event is sent when the light level changes from one side of the threshold to the other.

## Using it

Adjust the pin and topics as needed.