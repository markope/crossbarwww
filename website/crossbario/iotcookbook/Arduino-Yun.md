<div class="topimage_container">
<img id="cookbook_home_topimage" src="../../static/img/iotcookbook/arduino_yun.jpg" alt="" class="header_img" />
</div>

This is the **Crossbar.io IoT Cookbook's Yun homepage**.

The material here introduces the [Arduino Yun](http://www.arduino.cc/en/Main/ArduinoBoardYun?from=Main.ArduinoYUN) and how to make it into a real IoT device by connecting to Crossbar.io. We also provide ready-to-go recipes for complete IoT components and apps based on the Yun and Crossbar.io.

We suggest you read the [Overview](Arduino-Yun-Overview) first.

If you just want generic access to the Yun's GPIO ports (read, write and monitor for changes), then do the [Quick Setup](Arduino-Yun-Quick-Setup) and use the [Generic Serial-to-WAMP bridge](Arduino Yun Generic Serial to WAMP Bridge).

If you want to do custome stuff, then take a look at the Specific Tutorials, or look whether we've already got your use case coverd with a Component or an Application.

## Getting Started

* [Overview](Arduino-Yun-Overview): an overview of the Yun, its features and the integration into IoT applications
* [Quick Setup](Arduino-Yun-Quick-Setup): a quick setup recipe
* [Generic Serial-to-WAMP bridge](Arduino Yun Serial to WAMP Bridge): access the Yun's GPIO pins via WAMP


## Basic Tutorials

A three part tutorial that shows how to hook up the Yun to Crossbar.io and communicate from any other WAMP component. Available for

* [Python](Arduino Yun Python Tutorial)
* [JavaScript/NodeJS](Arduino Yun JavaScript Tutorial)


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

## Specific Tutorials

* [System Recovery](Arduino Yun System Recovery): resetting the Yun's WiFi settings and the Arduino part, restoring factory defaults for the Linux part
* [System Update](Arduino Yun System Update): getting the most up-to-date version of the Yun's Linux operating system
* [Establishing Network Connectivity](Arduino Yun Network Connectivity): Connecting your Yun to ethernet & WiFi
* [Connecting via SSH](Arduino Yun SSH Access): connecting via SSH to administrate the Yun
* [Expanding disk space](Arduino-Yun-Expanding-Disk-Space): using a microSD card to expand the storage on the Yun
* [Disabling the serial bridge](Arduino-Yun-Disable-Bridge): disabling the default serial bridge so we can use serial for our own
* [Setting up Autobahn|Python](Arduino-Yun-AutobahnPython-Setup): setting up Autobahn|Python and Twisted for Python programming on the Yun
* [Setting up Autobahn|JS](Arduino-Yun-AutobahnJS-Setup): setting up Autobahn|JS and Node for JavaScript programming on the Yun
* [Preparing an image](Arduino-Yun-Prepare-Image): how to create an extroot overlay SD card image for distribution
