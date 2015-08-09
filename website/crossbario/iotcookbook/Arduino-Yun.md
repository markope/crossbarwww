<div class="topimage_container">
<img id="cookbook_home_topimage" src="../../static/img/iotcookbook/arduino_yun.jpg" alt="" class="header_img" />
</div>

**The IoT Cookbook: Arduino Yun**

1. [Getting Started](#getting-started)
1. [Basic Tutorial](#basic-tutorial)
1. [Components](#components)
1. [Apps](#apps)
1. [Recipes](#recipes)

The material here introduces the [Arduino Yun](http://www.arduino.cc/en/Main/ArduinoBoardYun?from=Main.ArduinoYUN), how to connect the Yun to Crossbar.io and how to talk to the Yun from any other WAMP component, such as a browser or a backend. We also provide ready-to-go recipes for complete IoT components and apps based on the Yun and Crossbar.io.

<!--
We suggest you read the [Overview](Arduino-Yun-Overview) first.

If you just want generic access to the Yun's GPIO ports (read, write and monitor for changes), then do the [Quick Setup](Arduino-Yun-Quick-Setup) and use the [Generic Serial-to-WAMP bridge](Arduino Yun Generic Serial to WAMP Bridge).

If you want to do custom stuff, then take a look at the Specific Tutorials, or look whether we've already got your use case coverd with a Component or an Application.
-->

## Getting Started

We recommend reading into the following to get some background info, get things installed and configured and actually get you feet wet and talk to your Yun from a browser:

* [Overview](Arduino-Yun-Overview): an overview of the Yun, its features and the integration into IoT applications
* [Quick Setup](Arduino-Yun-Quick-Setup): a quick setup recipe using the Autobahn-Yun image we provide
* [Generic Serial-to-WAMP bridge](Arduino Yun Serial to WAMP Bridge): access the Yun's GPIO pins via WAMP


## Basic Tutorial

A basic, three part tutorial that shows how to hook up the Yun to Crossbar.io and communicate from any other WAMP component.

Available for

* [Python / Twisted](Arduino Yun Python Tutorial)
* [JavaScript / NodeJS](Arduino Yun JavaScript Tutorial)

You'll learn how to write code running on the microcontroller talking to code running on the Yun's main CPU talking to Crossbar.io and any other WAMP component running somewhere.


## Components

Arduino Yun based building blocks for use in IoT applications.

### Input Components

Sensor components that expose a sensor such as a ambient light, tilt or accelerometer by publishing WAMP events when sensor values change and that can be processed by other WAMP components.

* [Accelerometer](Arduino Yun Accelerometer) - receive raw acceleromter data or events when a certain threshold has been exceeded
* [Tilt Sensor](Arduino Yun Tilt Sensor) - get notifications when the state of a Tinkerkit tilt sensor changes
* [Ambient Light](Arduino Yun Ambient Light Sensor) - get the current light level and receive notifications if a threshold value is crossed
* [Buttons](Arduino Yun Buttons) - receive events for up to 6 buttons connected to a Yun
* [Potentiometer](Arduino Yun Potentiometer) - get the value and updates from up to 6 Tinkerkit potentiometers

### Output Components

Actuator components that usually expose an actuator such as a light, buzzer or servo motor as a procedure remotely callable via WAMP from other WAMP components.

* [Lights](Arduino Yun Lights) - light up up to 6 LEDs remotely (or any other modules which accept digital write)

## Apps

Apps combine one or more components into a IoT solution. They usually have code run non-device WAMP components as well, that provides the backend application logic.

* [Alarm](Apps Alarm) - simple alarm system. Uses accelerometers, buttons, signallight components and comes with a Web frontend (for desktop + mobile). Can include Arduino Yun, [[Raspberry Pi]] and [[Tessel]]

## Recipes

The recipes here each cover specific tasks related to handling the Yun.

* [System Recovery](Arduino Yun System Recovery): restoring the Yun's firmware and resetting Wifi settings
* [System Update](Arduino Yun System Update): getting the most up-to-date version of the Yun's Linux operating system
* [Establishing Network Connectivity](Arduino Yun Network Connectivity): Connecting your Yun to ethernet & WiFi
* [Connecting via SSH](Arduino Yun SSH Access): connecting via SSH to administrate the Yun
* [Expanding disk space](Arduino-Yun-Expanding-Disk-Space): using a microSD card to expand the storage on the Yun
* [Disabling the serial bridge](Arduino-Yun-Disable-Bridge): disabling the default serial bridge so we can use serial for our own
* [Setting up Autobahn|Python](Arduino-Yun-AutobahnPython-Setup): setting up Autobahn|Python and Twisted for Python programming on the Yun
* [Setting up Autobahn|JS](Arduino-Yun-AutobahnJS-Setup): setting up Autobahn|JS and Node for JavaScript programming on the Yun
* [Preparing an image](Arduino-Yun-Prepare-Image): how to create an extroot overlay SD card image for distribution
