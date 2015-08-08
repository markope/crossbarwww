This page describes how to install the necessary software on a Yun to enable remote control of the Yun's Arduino pins via WAMP.  For an overview of all materials we have concerning the Yun, see

* [Arduino Yun Links](Arduino Yun)

<div class="topimage_container">
   <img class="topimage" src="../../static/img/iotcookbook/remote_gpio_arduino_yun.jpg" alt="">   
</div>


## The big picture

The GPIO pins are managed by the Arduino MCU part of the Yun, while all network communcation is managed by the MIPS/Linux) part. 

To get remote control, we need to pass data from the MUC to the MIPS/Linux part, and the send this over the network.

We use WAMP for the remote communication.

For the MCU-MIPS bridge we use the [firmata](https://github.com/firmata/protocol) protocol. 

There is an Arduino implementation of this, which the MCU part runs. There are various implementations which we could run on the Linux side. In the end, using Node.js with `arduino-firmata` and Autobahn|JS to provide WAMP connectivity proved easiest.

This does not mean that you have to use JavaScript for your application: we provide access via WAMP to all the pins, so that you can write your actual control code in any language with a WAMP implementation. (You may at some point move control code onto the Yun itself, at which point the implementation languages become important again.)

## Installation

We offer [Quick Setup instructions](Arduino Yun Quick Setup) which use an image you can write to SD card, and which already has the necessary software for the serial-to-WAMP bridge installed for the Linux side.

For the MCU, you need to [install Firmata](Arduino Yun Installing Firmata).

You can also set things up manually. We cover the necessary steps below, at the end of this page, in 'Installation (manual)'. 

## The bridge code

We can now control the Arduino GPIO pins from Node.js - and the Node.js code in turn can communicate with any WAMP component. 

This is fine, but we really want to be able to develop on our own machines and in more comfort - and in our language of choice.

This is made possible by the serial-to-WAMP-bridge code which we offer for running in Node.js. With this, input and output is run via standardized WAMP publishes and subscriptions, so that you can just set up the bridge once on the Yun and then develop components which use the pins whereever you want.

The code for this is part of the SD card image used as part of [Quick Setup](Arduino Yun Quick Setup). If you've installed manually, then getting this onto the Yun is part of the instructions there (down below).

### Configuring the connection to Crossbar.io

The code for the access to the GPIO pins can be kept generic, but you need to configure the connection to a Crossbar.io instance. 

This is done via a config file in the FAT32 partition. This is a simple text file (`config`) in the `brige_config` directory, with one config option per line. You can edit this when the SD card is mounted on your dev machine (e.g. diretly after you've written it), or using vi when you're logged in via SSH.

An example config file containing just the required information would be 

```
routerURL: https://demo.crossbar.io
realm: iot_cookbook
```

+ deviceID (authID for WAMP-CRA)
+ WAMP-CRA secret

which means that the serial-to-WAMP bridge will attempt to establish a WAMP connection to a Crossbar.io instance at `https://demo.crossbar.io` and to the realm `iot_cookbook` on that instance.

### The API

The API exposes procedures in the format 

```
io.crossbar.examples.yun.<device_ID>.firmata.<procedure_name>
```

The procedures are:

* `set_mode`: set the mode for a pin, with the possible values `in` (you actively read from the pin), `out` (you write to the pin) and `watch` (monitor in value of the pin)
* `digital_read`: Read the state of a pin connected to digitial input device. Returns a Boolean.
* `digital_write`: Write the state of a pin connected to a digital output device. Takes a Boolean.
* `analog_read`: Read the state of a pin connected to an analog input device. Returns a numeric value, where the range depends on the input device .
* `analog_write`:  Write the state of a pin connected to an analog output device. Takes a numeric value, where the range depends on the output device.
* `servo_write`
* `reset`: reset the state of the arduino part

For pins which have been set to `watch`, value changes are published to the topics

```
io.crossbar.examples.yun.<device_ID>.firmata.on_analog_changed
```

and (*presently unimplemented*) 

```
io.crossbar.examples.yun.<device_ID>.firmata.on_digital_changed
```

## Manual Installation 

To get things working you need to

* disable the standard console control on serial
* install Node.js and depencies on the Linux system
* install the firmata code on the Arduino MCU

This requires:

* [extending the disk space](Arduino-Yun-Extending-Disk-Space) on the Yun
* a Yun with internet access
* shell access to the Yun
* Node.js installed on your computer
* the Arduino IDE installed on your computer

### Disable Console on Serial

See [Disable Bridge](Arduino Yun Disable Bridge).


### Installing software on the Linux system

Update `opkg`

```shell
opkg update
```

Then install Node.js

```shell
opkg install node
```

... and now might be a good time to get a cup of coffee or tea - and probably finish drinking it before the next step. Things may take so long here that you think the system has hung (especially if you have a slow SD card).

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

Before moving these over to the Yun, we need to remove the serialport component from arduino-firmata, since we want to use the one we already installed. To do so delete the `serialport` directory in the `arduino-firmata` folder. 

Then copy over the two modules using `scp`, e.g. from the `node-modules` directory open in a shell do

```shell
scp -r ./arduino-firmata root@192.168.1.150.local:/usr/lib/node_modules
scp -r ./autobahn root@192.168.1.150.local:/usr/lib/node_modules
```

The code for the serial-to-WAMP bridge can be found in the [crossbarexamples GitHub repository](https://github.com/crossbario/crossbarexamples) under `iotcookbook`. You need to clone this (or [download it as a ZIP file](https://github.com/crossbario/crossbarexamples/archive/master.zip)).

From this you need to get `remote_gpio_yun.js` ([direct link](---XXXX ADD LINK ----)) (in `crossbarexamples/iotcookbook/device/yun/remote_gpio`) onto the Yun.

First modify this so that it connects to your Crossbar.io instance, then do

```shell
scp remote_gpio_yun.js root@<IP_of_your_Yun>:~/
```

from a shell open to the above directory.

Then run this

```shell
nodejs remote_gpio_yun.js
```


### Installing software on the Arduino MCU

You need to [install Firmata](Arduino Yun Installing Firmata).



# Next

For examples of how remote GPIO can be used see e.g.

* [Alarm App](Apps Alarm)
* [Buttons](Arduino Yun Buttons)
* [Lights](Arduino Yun Lights)