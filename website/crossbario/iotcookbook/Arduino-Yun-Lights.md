The Arduino Yun Lights component allows the remote controls of up to 6 Tinkerkit LED modules (or other modules which can be accessed via digital write) via WAMP.

## Trying it out

The code for this can be found in the [crossbarexamples GitHub repository](https://github.com/crossbario/crossbarexamples) under `iotcookbook`. You need to clone this (or [download it as a ZIP file](https://github.com/crossbario/crossbarexamples/archive/master.zip)).

Open a shell for the component directory. 

Start up Crossbar.io:

```shell
crossbar start
```

This also serves a frontend where you can trigger the lights at

```
http://localhost:8080
```

In `lights_yun.js`, add the URL of the machine on which Crossbar.io runs:

```javascript
var connection = new autobahn.Connection({
   url: "ws://<URL OF YOUR CROSSBAR INSTANCE>/ws", // replace with the url of your crossbar instance
   realm: "iot_cookbook"
});
```

You need to have completed the setup for remote GPIO access on the Yun - see [[Arduino Yun Remote GPIO]]. 

Transfer `lights_yun.js` onto the Yun, e.g. by doing 

```console
scp lights_yun.js root@<IP of your Yun>:~/
```

Then run `lights_yun.js` 

```shell
node lights_yun.js
```

This should log

```shell
Arduino Yun Lights starting ...
Arduino connected (over /dev/ttyATH0, board version 2.3)
Connecting to router ...
Router connected. Session ID: 717010044
procedure 'io.crossbar.examples.yun.lights.set_light_state' registered
```

Once this is running, open the browser console for the frontend page and trigger the lights via the buttons. 

Use the 'disco' mode to get all of them blinking at once!

## The API

The lights component exposes a procedure for toggling the lights under

```
io.crossbar.examples.yun.lights.set_light_state
```

This takes the Tinkerkit shield output label as its value, i.e. "O0" - "O5". (See for the code how this corresponds to the actual GPIO pins on the Yun.)

## Using it

In your own project:

* Adapt the topic under which the lights can be triggered to your own needs.