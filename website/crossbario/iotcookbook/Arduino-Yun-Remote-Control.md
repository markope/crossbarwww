This page describes how to install the necessary software on a Yun to enable remote control of the Yun's Arduino pins via WAMP.

## Overview

The GPIO pins are managed by the Arduino MCU part of the Yun, while all network communcation is managed by the MIPS part. 

To get remote control, we need to pass data from the MUC to the MIPS/Linux part, and the send this over the network.

We use WAMP for the remote communication.

For the MCU-MIPS bridge we use the [firmata](https://github.com/firmata/protocol) protocol. 

There is an Arduino implementation of this, which the MCU part runs. There are various implementations which we could run on the Linux side. In the end, using Node.js with `arduino-firmata` and Autobahn|JS to provide WAMP connectivity proved easiest.

This does not mean that you have to use JavaScript for your application: we provide access via WAMP to all the pins, so that you can write your actual control code in any language with a WAMP implementation. (You may at some point move control code onto the Yun itself, at which point the implementation languages become important.)

To get things working you need to

* disable the standard console control on serial
* install Node.js and depencies on the Linux system
* install the firmata code on the Arduino MCU

This requires:

* [extending the disk space](Arduino-Yun-Extending-Disk-Space) on the Yun
* Yun with internet access
* shell access to the Yun
* Node.js installed on your computer
* the Arduino IDE installed on your computer

## Disable Console on Serial

We are using the serial connection between the MCU and the CPU. By default, there is a console attached on the Linux side to the serial, and we need to disable that.

Edit the file `/etc/inittab` and comment the following line (by preceding it with `#`):

```shell
# ttyATH0::askfirst:/bin/ash --login
```

> The Linux SoC (CPU) and the Atmel MCU are connected via a UART (a serial connection) which maps to the device `/dev/ttyATH0` on the Linux side and the [serial stream](http://arduino.cc/en/Reference/Serial) class `Serial1` on the Arduino side. The default `inittab` entry on the Linux side will start a shell connected to that serial port when Linux boots. Then, when your sketch starts the Arduino Yun bridge library (by doing `Bridge.begin()`), the bridge library writes a command to the serial that will in turn start a script on the Linux side which then connects to the serial port. That Linux script is essentially the Linux-side part of the Yun bridge library and will keep on running regardless of wether you reload a new sketch to the MCU or reset the MCU. It will keep on running until you reset the CPU or reboot Linux (or manually kill the script). However, as long as there is a script running and using the serial port, we cannot use the serial for our purposes. The commenting of the `inittab` line will disable starting a shell on the serial port altogether in the first place. **This means we can use the serial port for our stuff, but it also means you won't be able to use the Yun brigde library anymore.**
> 

and reboot Linux:

```shell
reboot
```

> Be patient, a reboot (either via the `reboot` command like above, or by doing a cold boot via power cycling or pressing the "Yun RST" button) can take 60-90s.
> 


## Installing software on the Linux system

Update `opkg` (yes, again: this doesn't persist agains reboots):

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

The other two packages need to be installed via Node.js - and the Yun does not have enough RAM for npm to do its job for these.

We need to install them on another system and copy them over to the Yun. So you need to create an installation directory on your PC/Laptop, and do 

```shell
npm install arduino-firmata
npm install autobahn
```

This gives you the node modules installed in the `node-modules` folder.

Before moving these over to the Yun, we need to remove the serialport component from arduino-firmata. To so do delete the `serialport` directory in the `arduino-firmata` folder. 

Then copy over the two modules using `scp`, e.g. from the `node-modules` directory open in a shell do

```shell
scp -r ./arduino-firmata root@192.168.1.150.local:/usr/lib/node_modules
scp -r ./autobahn root@192.168.1.150.local:/usr/lib/node_modules
```

## Installing software on the Arduino MCU

The Arduino MCU is accessed via the [Arduino IDE](http://www.arduino.cc/en/Main/Software), which is available cross-platform.

Access can, in principle, be via wi-fi or USB. Since we've (needed to) disable the standard serial bridge, we need to use USB.

Connect your Yun via USB, start the Arduino IDE and check that your Yun has been recognized. It should be listed under `Tools --> board`, and you should find a connection port under `Tools --> port` which is labeled `Yun`. (On Windows this is a COM port - and it may take a couple of tries to get recognized.)

To check that your connection is working, it's easiest to use the [blinky code](http://www.arduino.cc/en/Tutorial/Blink?from=Tutorial.BlinkingLED) provided by the Arduino project, which makes the LED L13 on the Yun, which is connected to one of the GPIO pins, blink (as the name suggests).

```c
/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
 
  This example code is in the public domain.
 */
 
// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
int led = 13;

// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);     
}

// the loop routine runs over and over again forever:
void loop() {
  digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);               // wait for a second
  digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);               // wait for a second
}
```

Paste this into the IDE, save it somewhere, verify it (which requires the previous saving step), and then upload it to the Yun. You should now have a blinking LED!

The firmata code we need can be found on [GitHub](https://raw.githubusercontent.com/firmata/arduino/master/examples/StandardFirmataYun/StandardFirmataYun.ino)
. As with the blinky code: paste, save, verify and upload.


## Checking that the Arduino and Linux side are communicating

To verify that the Arduino - Linux firmata-over-serial connection works, it's easiest to run a blinky version in Node.js. Save the following in a file, e.g. `node-blinky.js` on the Yun:

```javascript
var ArduinoFirmata = require('arduino-firmata');
var arduino = new ArduinoFirmata().connect('/dev/ttyATH0');
arduino.on('connect', function(){
  console.log("connect!! "+arduino.serialport_name);
  console.log("board version: "+arduino.boardVersion);
var stat = true
  setInterval(function(){
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

## The remote control code

We can now control the Arduino GPIO pins from Node.js - and the Node.js code in turn can communicate with any WAMP component. 

This is fine, but we really want to be able to develop on our own machines and in more comfort - and in our language of choice.

This is made possible by the serial-to-WAMP-bridge code which we offer for running in Node.js. With this, input and output is run via standardized WAMP publishes and subscriptions, so that you can just set up the bridge once on the Yun and then develop components which use the pins whereever you want.
