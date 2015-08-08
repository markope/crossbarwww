The Arduino Yun Accelerometer component publishes the raw accelerometer data from a Tinkerkit accelerometer module via WAMP.

<div class="topimage_container">
   <img class="topimage" src="../../static/img/iotcookbook/accelerometer_arduino_yun.png" alt="">   
</div>

## Trying it out

The code for this can be found in the [crossbarexamples GitHub repository](https://github.com/crossbario/crossbarexamples) under `iotcookbook`. You need to clone this (or [download it as a ZIP file](https://github.com/crossbario/crossbarexamples/archive/master.zip)).

Open a shell for the component directory. 

Start up Crossbar.io:

```shell
crossbar start
```

This also serves a frontend where you can view the accelerometer data logged at

```
http://localhost:8080
```

In `accelerometer_yun.js`, add the URL of the machine on which Crossbar.io runs:

```javascript
var connection = new autobahn.Connection({
   url: "ws://<URL OF YOUR CROSSBAR INSTANCE>/ws", // replace with the url of your crossbar instance
   realm: "iot_cookbook"
});
```

You need to have completed the setup for remote GPIO access on the Yun - see [[Arduino Yun Remote GPIO]], and have a Tinkerkit accelerometer connected. (This is expected on pins 2 and 3 / I2/3 on the Tinkerkit shield.)

Transfer `accelerometer_yun.js` on the Yun, e.g. by doing 

```console
scp accelerometer_yun.js root@<IP of your Yun>:~/
```

Then run `accelerometer_yun.js` 

```shell
node accelerometer_yun.js
```

This should log

```shell
Arduino Yun Accelerometer starting ...
Arduino connected (over /dev/ttyATH0, board version 2.3)
Connecting to router ...
Router connected. Session ID: 1595783623
```

Once this is running, open the browser console for the frontend page, and you'll see the raw accelerometer data logged as it is received.

```javascript
received accelerometer data Object {y: 566, x: 551}
received accelerometer data Object {y: 566, x: 552}
received accelerometer data Object {y: 565, x: 551}
```

and when you move the accelerometer beyond the acceleration threshold

```javascript
received accelerometer data Object {y: 978, x: 504}
alarm activated!
received accelerometer data Object {y: 772, x: 543}
alarm activated!
received accelerometer data Object {y: 753, x: 564}
alarm activated!
```

## The API

The accelerometer component publishes the raw accelerometer data as JSON to the topic

```
io.crossbar.examples.yun.accelerometer.on_accelerometer_data
```

## Using it

In your own project:

* Adapt the topic which is sent by `accelerometer.js` to your own needs.