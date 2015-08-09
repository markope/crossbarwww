The Arduino Yun Potentiometer component publishes events when the state of a Tinkerit potentiometer changes.

<div class="topimage_container">
   <img class="topimage" src="../../static/img/iotcookbook/yun_potentiometer.jpg" alt="">   
</div>

## Trying it out

The code for this can be found in the [crossbarexamples GitHub repository](https://github.com/crossbario/crossbarexamples) under `iotcookbook`. You need to clone this (or [download it as a ZIP file](https://github.com/crossbario/crossbarexamples/archive/master.zip)).

You need to have at least one Tinkerkit potentiomete, which as a default should be connected to 'I0' on the Tinkerkit shield (pin 0).

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

You need to set up the Yun for [using AutobahnJS](Arduino Yun AutobahnJS Setup), including setting up Firmata on the MCU part of the Yun.

Transfer `potentiometer_yun.js` on the Yun, e.g. by doing 

```console
scp potentiometer_yun.js root@<IP of your Yun>:~/
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
potentiometer value currently is: 0 20
```

and when you turn the potentiometer something like

```
potentiometer value change: [0, 24]
potentiometer value change: [0, 26]
potentiometer value change: [0, 28]
potentiometer value change: [0, 31]
potentiometer value change: [0, 33]
```

## The API

The component provides one procedure

```
io.crossbar.examples.yun.potentiometer.get_potentiometer_value
```

which takes the pin the potentiometer is connected to as an argument and returns the current potentiometer value (0 - 100),

and publishes to one topic

```
io.crossbar.examples.yun.potentiometer.on_value_change
```

which provides the pin of the potentiometer where the value change occured adn the current potentiometer value (0 - 100).


## Using it

Adjust the pin and topics as needed, add potentiometers.