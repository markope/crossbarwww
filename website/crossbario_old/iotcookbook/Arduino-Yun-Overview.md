This page provides some basic information about the Arduino Yun. For an overview of all materials we have concerning the Yun, please see [here](Arduino Yun).

# What is the Arduino Yun?

The [Arduino Yun](http://www.arduino.cc/en/Main/ArduinoBoardYun?from=Main.ArduinoYUN) is an open-source, single-board computer that combines a microcontroller with a CPU and Wifi:

<figure>
   <img style="width: 480px;" src="/static/img/iotcookbook/yun/arduino-yun.jpg" alt="Arduino Yun" class="imgCentered">
</figure>

The Yun actually is *2 computers in one*:

  * a tiny **8-Bit AVR MCU** ([ATmega32u4](http://www.atmel.com/dyn/resources/prod_documents/7766S.pdf) with 32kB Flash and 2.5kB RAM running at 16MHz)
  * a small **32-Bit MIPS CPU** ([Atheros AR9331](http://www.eeboard.com/wp-content/uploads/downloads/2013/08/AR9331.pdf) with 16MB Flash and 64MB RAM running at 400MHz)

The MCU runs in *hard* real-time: you can use it to e.g. directly control servo motors or interface to sensors. The CPU on the other hand is powered by an embedded Linux ([Linino](https://github.com/arduino/linino)) that does not run in hard real-time, but is **capable of doing full flavored TCP/IP networking over Ethernet and Wifi**. The MCU and the CPU are connected via a serial interface.

<img src="../../static/img/iotcookbook/yun/yun_diagram.png" alt="">

The Yun's CPU and RAM are enough to run things like Node.js (but not much more). The biggest limitation are the 16MB flash, of which 8MB are reserved as a a recovery partition. We provide a tutorial for how to set up the Yun to use a microSD card for its filesystem.

## Connecting the Yun to the World

Now, while the Arduino Yun (like all Arduinos) already allows you to create awesome hardware oriented projects, wouldn't it be great if you could connect your Arduino Yun to other devices, browsers or mobile apps, communicating in *(soft) real-time* over the Web?

We'll be making the Yun into a real IoT device by connecting it to Crossbar.io. This allows the Yun to publish real-time events e.g. to distribute sensor readings, and securily control the Yun with remote procedure calls from any other WAMP component <b>(get the full presentation <a href="../../static/img/docs/design/crossbar_iot_integration/crossbar_iot_integration.pdf">Crossbar.io/Yun integration in 3 slides</a>)</b>.

<img src="../../static/img/iotcookbook/crossbar_iot_integration_1.png" alt="">

[WAMP](http://wamp.ws/) uses WebSocket as a transport and allows bidirectional real-time messaging on the Web and WAMP adds asynchronous [Remote Procedure Calls](http://wamp.ws/faq/#rpc) and [Publish & Subscribe](http://wamp.ws/faq/#pubsub) on top of WebSocket.

Here is an example of what you can do with Arduino Yun and WAMP:

 * stream sensor readings in real-time from the Arduino Yun via WebSocket to HTML5 browsers on desktop and mobile
 * control LEDs directly from your browser (again in real-time with very small latency)

<div class="videoBox">
   <iframe class="video" type="text/html" src="http://www.youtube.com/embed/Egvu4jL_Wlo?version=3&vq=hd720&frameborder=0&allowfullscreen&autohide=2&modestbranding=1&showinfo=0&rel=0&origin=http://crossbar.io" frameborder="0"/></iframe>
   <div class="videoCaption">Arduino Yun Real-time Charting over WebSocket with Autobahn</div>
</div>


> The demo shows a shield on the Yun with 2 potis, 3 LEDs and 2 buttons, which are controlled from a simple sketch running on the Arduino. The sketch communicates over serial with Autobahn|Python running on the Linux side of the Yun, providing WAMP connectivity. And Autobahn in turn runs as a bridge that shuffles data from/to serial and to WebSocket/WAMP clients (here, Chrome running on desktop and on Nexus 4) connecting to Autobahn over Wifi.
>

We'll give you step-by-step instructions for how to set up a Yun to work with WAMP. Specifically, we're going to set up Node.js and Autobahn|JS to enable you to access the Arduino pins on the Yun remotely (from any language with a WAMP implementation).

## Next

- [Quick Setup](Arduino-Yun-Quick-Setup)
