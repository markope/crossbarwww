The Arduino Yun Potentiometer component publishes events when the state of a Tinkerit potentiometer changes.

<div class="topimage_container">
   <img class="topimage" src="../../static/img/iotcookbook/tilt_arduino_yun.jpg" alt="">   
</div>

## Trying it out

The code for this can be found in the [crossbarexamples GitHub repository](https://github.com/crossbario/crossbarexamples) under `iotcookbook`. You need to clone this (or [download it as a ZIP file](https://github.com/crossbario/crossbarexamples/archive/master.zip)).

You need to have one Tinkerkit potentiometer connected to 'I0' on the Tinkerkit shield (pin 0).

Open a shell for the component directory. 

Start up Crossbar.io:

```shell
crossbar start
```

This also serves a frontend where you can view the potentiometer data logged at

```
http://localhost:8080
```

In `potentiometer_yun.js`, add the URL of the machine on which Crossbar.io runs:

```javascript
var connection = new autobahn.Connection({
   url: "ws://<URL OF YOUR CROSSBAR INSTANCE>/ws", // replace with the url of your crossbar instance
   realm: "iot_cookbook"
});
```

You need to have completed the setup for remote GPIO access on the Yun - see [[Arduino Yun Remote GPIO]]. 

Transfer `potentiometer_yun.js` on the Yun, e.g. by doing 

```console
scp potentiometer_yun.js pi@<IP of your Yun>:~/
```

Then run `potentiometer_yun.js` using Node.js

```shell
node potentiometer_yun.js
```

This should log something like

```
Arduino Yun Potentiometer starting ...
Arduino connected (over /dev/ttyATH0, board version 2.3)
Connecting to router ...
Router connected. Session ID: 1431639925
io.crossbar.examples.yun.potentiometer.get_potentiometer_value registered
```

Once this is running, open the browser console for the frontend page and reload the page. You shoud see something like 

```
connected
potentiometer value currently is:  20
```

and when you turn the potentiometer

```
Value changed to:  22
Value changed to:  25
Value changed to:  28
Value changed to:  30
Value changed to:  32
Value changed to:  35
Value changed to:  37
Value changed to:  39
Value changed to:  43
Value changed to:  45
```

## The API

The component provides one procedure

```
io.crossbar.examples.yun.potentiometer.get_potentiometer_value
```

which returns the current potentiometer value (0 - 100),

and publishes to one topic

```
io.crossbar.examples.yun.potentiometer.on_value_change
```

which provides the current potentiometer value (0 - 100).


## Using it

Adjust the pin and topics as needed.