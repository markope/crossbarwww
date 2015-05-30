<div class="topimage_container">
   <img class="topimage" src="../../static/img/iotcookbook/arduino_yun.jpg" alt="">   
</div>

The [Arduino Yun](http://www.arduino.cc/en/Main/ArduinoBoardYun?from=Main.ArduinoYUN) is a Linux computer + microcontroller with built-in wifi which runs OpenWRT (a Linux flavor used mainly on DSL routers).

* [Overview](Arduino-Yun-Overview): a more detailed overview of the Yun and its features
* [Basic setup](Arduino-Yun-Basic-Setup) takes you through connecting to the Yun and updating its software
* [Extending the disk space](Arduino-Yun-Expanding-Disk-Space) explains the steps to configure the Yun to use a microSD card as storage (necessary due to the exteremely limited onboard flash)

## Generic Control of GPIO

* [Remote GPIO](Arduino Yun Remote GPIO) gives access to the GPIO pins on the Arduino Yun. Each pin has a pre-set associated endpoint.

## Components

**Input**

* [Accelerometer](Arduino Yun Accelerometer) - receive raw acceleromter data or events when a certain threshold has been exceeded
* [Tilt Sensor](Arduino Yun Tilt Sensor) - get notifications when the state of a Tinkerkit tilt sensor changes
* [Ambient Light](Arduino Yun Ambient Light Sensor) - get the current light level and receive notifications if a threshold value is crossed
* [Buttons](Arduino Yun Buttons) - receive events for up to 6 buttons connected to a Yun
* [Potentiometer](Arduino Yun Potentiometer) - get the value and updates from up to 6 Tinkerkit potentiometers

**Output**

* [Lights](Arduino Yun Lights) - light up up to 6 LEDs remotely (or any other modules which accept digital write)

## Apps

* [Alarm](Apps Alarm) - simple alarm system. Uses accelerometers, buttons, signallight components and comes with a Web frontend (for desktop + mobile). Can include Arduino Yun, [[Raspberry Pi]] and [[Tessel]]