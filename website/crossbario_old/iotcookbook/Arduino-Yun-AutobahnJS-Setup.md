This recipe shows you how to install Autobahn|JS on the Yun in order to get WAMP connectivity for JavaScript/Node.js components on the Yun. This communicates with the firmata code on the MCU.

> Note: If you've completed the [Quick Setup](Arduino Yun Quick Setup), then Autobahn|JS is already installed. In this case you only need to set up Firmata on the MCU

## Installation on the Yun

Update `opkg`

```shell
opkg update
```

Then install Node.js

```shell
opkg install node
```

... and now might be a good time to get a cup of coffee or tea - and probably finish drinking it before the next step. Things may take so long here that you think the system has hung (in part depending on the access characteristics of your microSD card).

In addition to Node.js, we need a few dependencies:

* node-serialport (to connect to the serial bridge)
* arduino-firmata (to connect to the firmata software on the Arduino part)
* autobahn (to give us WAMP)

Unfortunately, only the first of these can be installed directly on the Yun:

```shell
opkg install node-serialport
```

## Installation with the help of a PC

The other two packages need to be installed via Node.js - and the Yun does not have enough RAM for npm to do its job for these.

We need to install them on another system and copy them over to the Yun. So you need to create an installation directory on your PC/Laptop and go into this, e.g.

```console
mkdir -p /tmp/yun
cd /tmp/yun
```

We install the node modules we need into this

```shell
npm install arduino-firmata
npm install autobahn
```

Before moving these over to the Yun, we need to remove the serialport component from arduino-firmata, since we want to use the one we already installed. To do so delete the `serialport` directory in the `arduino-firmata` folder, e.g. by doing (assumes a Unix-y shell):

```shell
rm -rf node_modules/arduino-firmata/node_modules/serialport/
```


Then copy over the modules using `scp` (replace the example IP with the IP of your Yun, this will require your password (same as for SSH, `arduino` as the default)):

```shell
scp -r ./node_modules/* root@192.168.1.141:/usr/lib/node_modules
```

To test that Autobahn|JS is working, on the Yun do:

```console
root@Arduino:~# node
> var autobahn = require('autobahn');
undefined
> autobahn.version
'0.9.6'
> 
```

## Installing Firmata on the MCU

Follow [these steps](Arduino Yun Installing Firmata).


## Testing the Firmata connection

On the Yun, save the following (e.g. as 'firmata_test.js') and run it using Node.js (e.g. `node firmata_test.js`). If all is well, a red LED on your Yun should be blinking in 300ms intervals.

```javascript
console.log("blinky starting ..");

var firmata = require('arduino-firmata');
var arduino = new firmata().connect('/dev/ttyATH0');

console.log("libraries loaded.");

arduino.on('connect', function () {
  console.log("serial connected: " + arduino.serialport_name);
  console.log("board version: " + arduino.boardVersion);

  var stat = true;
  setInterval(function () {
    console.log(stat);
    arduino.digitalWrite(13, stat);
    arduino.digitalWrite(12, !stat);
    stat = !stat;  // blink
  }, 300);
});
```
