This is the **Crossbar.io IoT Cookbook's Yun homepage**.

The material here introduces the [Arduino Yun](http://www.arduino.cc/en/Main/ArduinoBoardYun?from=Main.ArduinoYUN) and how to make it into a real IoT device by connecting to Crossbar.io. We also provide ready-to-go recipes for complete IoT components and apps based on the Yun and Crossbar.io.


## Introduction

The [Arduino Yun](http://www.arduino.cc/en/Main/ArduinoBoardYun?from=Main.ArduinoYUN) is an open-source, single-board computer that combines a microcontroller with a CPU and Wifi:

<div class="topimage_container">
   <img class="topimage" src="../../static/img/iotcookbook/arduino_yun.jpg" alt="">   
</div>

The CPU runs a Linux flavor and has full TCP/IP networking capabilities. The microcontroller (MCU) runs in hard real-time and can talk to the CPU via an onboard serial connection:

<img src="../../static/img/iotcookbook/yun/yun_diagram.png" alt="">

Check out the [Overview](Arduino-Yun-Overview) for a more detailed discussion of the Yun and its features.


## Integration with Crossbar.io

We'll be making the Yun into a real IoT device by connecting it to Crossbar.io. This allows the Yun to publish real-time events e.g. to distribute sensor readings, and securily control the Yun with remote procedure calls from any other WAMP component:

<img src="../../static/img/iotcookbook/crossbar_iot_integration_1.png" alt="">   

## Getting Started

* [Overview](Arduino-Yun-Overview):
    a more detailed overview of the Yun and its features
* [Basic setup](Arduino-Yun-Basic-Setup) takes you through connecting to the Yun and updating its software
* [Expanding disk space](Arduino-Yun-Expanding-Disk-Space): using a microSD card to expand the storage on the Yun
* [Disable the serial bridge](Arduino-Yun-Disable-Bridge): disabling the default serial bridge so we can use serial for our own
* [Setup Autobahn|Python](Arduino-Yun-AutobahnPython-Setup): setting up Autobahn|Python and Twisted for Python programming on the Yun
* [Setup Autobahn|JS](Arduino-Yun-AutobahnJS-Setup): setting up Autobahn|JS and Node for JavaScript programming on the Yun


## Tutorials

* [Arduino Yun Tutorial](Arduino Yun Tutorial): a three part tutorial that shows how to hook up the Yun to Crossbar.io and communicate from any other WAMP component
* [Remote GPIO](Arduino Yun Remote GPIO): generic access to the Yun's GPIO pins from WAMP

## Components

### Input Components

* [Accelerometer](Arduino Yun Accelerometer) - receive raw acceleromter data or events when a certain threshold has been exceeded
* [Tilt Sensor](Arduino Yun Tilt Sensor) - get notifications when the state of a Tinkerkit tilt sensor changes
* [Ambient Light](Arduino Yun Ambient Light Sensor) - get the current light level and receive notifications if a threshold value is crossed
* [Buttons](Arduino Yun Buttons) - receive events for up to 6 buttons connected to a Yun
* [Potentiometer](Arduino Yun Potentiometer) - get the value and updates from up to 6 Tinkerkit potentiometers

### Output Components

* [Lights](Arduino Yun Lights) - light up up to 6 LEDs remotely (or any other modules which accept digital write)

## Apps

* [Alarm](Apps Alarm) - simple alarm system. Uses accelerometers, buttons, signallight components and comes with a Web frontend (for desktop + mobile). Can include Arduino Yun, [[Raspberry Pi]] and [[Tessel]]