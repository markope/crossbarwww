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

### AutobahnJS

We offer [Quick Setup instructions](Arduino Yun Quick Setup) which use an image you can write to SD card, and which already has all the preparations for the serial-to-WAMP bridge installed for the Linux side. Otherwise you need to get AutobahnJS working on the Yun for the following.

### The bridge code

Get the [bridge code](https://github.com/crossbario/crossbarexamples/tree/master/iotcookbook/device/yun/serial_to_wamp) onto the Yun. If you've mounted the Yun's file system on your PC, just copy it over. Otherwise you can do

```shell
scp serial_to_wamp.js root@192.168.1.141:~/
```

from the directory the code is in (and where you replace the above IP with that of your Yun).

### The MCU code

For the MCU, you need to [install Firmata](Arduino Yun Installing Firmata).

### Running things

To run the bridge, just do 

```shell
node serial_to_wamp.js
```

## Configuring the connection to Crossbar.io

The code for the access to the GPIO pins can be kept generic, but you need to configure the connection to a Crossbar.io instance. 

This is done via a config file in the same directory as the serial bridge code. This is a simple text file (`config`), with one config option per line. 

The provided example config file is

```
routerUrl: https://demo.crossbar.io
realm: iot_cookbook
deviceId: my_yun
```
which means that the serial-to-WAMP bridge will attempt to establish a WAMP connection to a Crossbar.io instance at `https://demo.crossbar.io` and to the realm `iot_cookbook` on that instance.

For all events and registrations it uses the deviceID. (This means that the deviceID needs to conform to the [rules for WAMP URIs](../docs/URI-Format).)

## The API

The API exposes procedures in the format 

```
io.crossbar.examples.yun.<device_ID>.firmata.<procedure_name>
```

The procedures are:

* `set_mode`: set the mode for a pin, with the possible values `in` (you actively read from the pin), `out` (you write to the pin) and `watch` (monitor the value of the pin)
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

> Note: It is possible to read from a pin which is watched - so you can combine automatic notifications for value changes with e.g. getting the current value on component startup without having to wait for the next value change.

## Testing and usage examples

The code for this in the [Crossbarexamples repository](https://github.com/crossbario/crossbarexamples/tree/master/iotcookbook/device/yun/serial_to_wamp) allows you to start a Crossbar.io instance to which the bridge can connect for development purposes.

This also serves an HTML page which attempts to read from an analog input and write to a digital output. This is mainly for illustrative purposes, to give you some examples for how the API can be used.

## Next

For examples of how remote GPIO can be used see e.g.

* [Alarm App](Apps Alarm)
* [Buttons](Arduino Yun Buttons)
* [Lights](Arduino Yun Lights)