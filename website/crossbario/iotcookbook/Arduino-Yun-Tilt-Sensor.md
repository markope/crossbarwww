The Arduino Yun Tilt Sensor component allows querying the current state of a Tinkerkit tilt sensor and publishes events when this state changes.

<div class="topimage_container">
   <img class="topimage" src="../../static/img/iotcookbook/tilt_arduino_yun.jpg" alt="">   
</div>

## Trying it out

The code for this can be found in the [crossbarexamples GitHub repository](https://github.com/crossbario/crossbarexamples) under `iotcookbook`. You need to clone this (or [download it as a ZIP file](https://github.com/crossbario/crossbarexamples/archive/master.zip)).

You need to have one Tinkerkit tilt sensor connected to 'I0' on the Tinkerkit shield (pin 0).

Open a shell for the component directory. 

Start up Crossbar.io:

```shell
crossbar start
```

This also serves a frontend where you can view the tilt sensor data logged at

```
http://localhost:8080
```

In `tilt_yun.js`, add the URL of the machine on which Crossbar.io runs:

```javascript
var connection = new autobahn.Connection({
   url: "ws://<URL OF YOUR CROSSBAR INSTANCE>/ws", // replace with the url of your crossbar instance
   realm: "iot_cookbook"
});
```

You need to have completed the setup for remote GPIO access on the Yun - see [[Arduino Yun Remote GPIO]]. 

Transfer `tilt_yun.js` on the Yun, e.g. by doing 

```console
scp tilt_yun.js pi@<IP of your Yun>:~/
```

The script is run using Node.js, so you need to have this installed ('opkg install node').

Then run `tilt_yun.js` 

```shell
node tilt_yun.js
```

This should log

```
Arduino Yun Tilt Sensor starting ...
Arduino connected (over /dev/ttyATH0, board version 2.3)
Connecting to router ...
Router connected. Session ID: 1595783623
```

Once this is running, open the browser console for the frontend page and reload the page. You shoud see 

```
connected
tilt state currently is:  false
```

and when you tilt the sensor

```
Tilt state changed to:  true
Tilt state changed to:  false
Tilt state changed to:  true
Tilt state changed to:  false
```

## The API

The component provides one procedure

```
io.crossbar.examples.yun.tilt.get_is_tilted
```

which does not require any arguments and returns a Boolean for the tilt state.

It also publishes changes in the tilt state to

```
io.crossbar.examples.yun.tilt.on_is_tilted
```

where the changed tilt state, as a Boolean, is sent as an argument.

## Using it

Adjust the pin and topics as needed.