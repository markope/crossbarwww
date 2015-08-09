For some uses cases we need the code implementing the Firmata protocol on the MCU.

The [Firmata](https://github.com/firmata/protocol) code for the MCU part of the Yun provides generic access to the GPIO pins on the Yun. It comes with the Arduino IDE, and libraries to connect to this exist for a large number of languages.

## Disable Console on Serial

The firmata code establishes its own serial bridge, so we need to [disable the standard bridge](Arduino Yun Disable Bridge)

## Connecting the Yun to the IDE

The Arduino MCU is accessed via the [Arduino IDE](http://www.arduino.cc/en/Main/Software), which is available cross-platform.

Access can, in principle, be via wi-fi or USB. Since we need to disable the standard serial bridge, we'll use USB.

Connect your Yun via USB, start the Arduino IDE and check that your Yun has been recognized. It should be listed under `Tools --> board`, and you should find a connection port under `Tools --> port` which is labeled `Yun`. (On Windows this is a COM port - and it may take a couple of tries to get recognized.)

If you want to check that your connection is working, then it's easiest to use the [blinky code](http://www.arduino.cc/en/Tutorial/Blink?from=Tutorial.BlinkingLED) provided by the Arduino project, which makes the LED L13 on the Yun, which is connected to one of the GPIO pins, blink (as the name suggests).

Paste this into the IDE, save it somewhere, verify it (which requires the previous saving step), and then upload it to the Yun. You should now have a blinking LED!

Once you've checked the connection (or are confident it's working without checking) you can continue with

## Installing firmata

The Arduino IDE already contains the Firmata code we need. You load this into a new IDE window by selecting "File" - "Examples" - "Firmata" - "StandardFirmataYun"

You need to verify & upload the code.

## Checking that the Arduino and Linux side are communicating

To verify that the Arduino - Linux firmata-over-serial connection works, it's easiest to run a blinky version in Node.js (so you need to have this as well as the dependencies [installed](Arduino Yun AutobahnJS Setup)). 

Save the following in a file, as e.g. `node-blinky.js` on the Yun:

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

and then run it

```shell
node node-blinky.js
```

You should now get same LED blinking as before - just controlled from the Linux side of the Yun.
