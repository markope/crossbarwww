The Arduino Yun Button component publishes events for presses on up to 6 Tinkerkit button modules via WAMP.

<div class="topimage_container">
   <img class="topimage" src="../../static/img/iotcookbook/buttons_arduino_yun.jpg" alt="">   
</div>

## Trying it out

The code for this can be found in the [crossbarexamples GitHub repository](https://github.com/crossbario/crossbarexamples) under `iotcookbook`. You need to clone this (or [download it as a ZIP file](https://github.com/crossbario/crossbarexamples/archive/master.zip)).

Open a shell for the component directory. 

Start up Crossbar.io:

```shell
crossbar start
```

This also serves a frontend where you can view the button data logged at

```
http://localhost:8080
```

In `buttons_yun.js`, add the URL of the machine on which Crossbar.io runs:

```javascript
var connection = new autobahn.Connection({
   url: "ws://<URL OF YOUR CROSSBAR INSTANCE>/ws", // replace with the url of your crossbar instance
   realm: "iot_cookbook"
});
```

Additionally, in the `buttons` array, only those parts corresponding to actually connected buttons should be commented in. Otherwise, with e.g. a connection pattern like `0--3--`, while a press on `0` will produce the correct event, a press on `3`will produce events for the unconnected buttons `1` and `2` in addition to `3`.

You need to set up the Yun for [using AutobahnJS](Arduino Yun AutobahnJS Setup), including setting up firmata on the MCU.

Transfer `buttons_yun.js` on the Yun, e.g. by doing 

```console
scp buttons_yun.js root@<IP of your Yun>:~/
```

Then run `buttons_yun.js` 

```shell
node buttons_yun.js
```

This should log

```
Arduino Yun Buttons starting ...
Arduino connected (over /dev/ttyATH0, board version 2.3)
Connecting to router ...
Router connected. Session ID: 1595783623
```

Once this is running, open the browser console for the frontend page and press some buttons. You'll see the button events logged:

```
Button pressed:  3
Button pressed:  0
Button pressed:  3
```


## The API

The buttons component publishes events for button presses to the topic

```
io.crossbar.examples.yun.buttons.button_pressed
```

with the button pressed in the arguments.

## Using it

In your own project:

* Adapt the topic which is sent by `buttons_yun.js` to your own needs.