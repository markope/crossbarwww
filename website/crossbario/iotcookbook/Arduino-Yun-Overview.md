This page provides some basic information about the Arduino Yun, as well as links to resources on how to

* [Do basic setup of the Yun]()
* [Expand the disk space to a microSD card]()
* [Install software to remote-control the Arduino pins]()


## What is the Arduino Yun?

The [Arduino Yun](arduino.cc/en/Main/ArduinoBoardYun) is a small embedded computer which can be used as a flexible platform for all kinds of hardware projects:

<figure>
   <img style="width: 480px;" src="{{ url_for('static', filename='img/blog/arduino-yun-getting-started-part-1/arduino-yun.jpg') }}" alt="Arduino Yun" class="imgCentered">
   <figcaption>Arduino Yun</figcaption>
</figure>

The Yun actually is *2 computers in one*:

  * a tiny **8-Bit AVR MCU** ([ATmega32u4](http://www.atmel.com/dyn/resources/prod_documents/7766S.pdf) with 32kB Flash and 2.5kB RAM running at 16MHz)
  * a small **32-Bit MIPS CPU** ([Atheros AR9331](http://www.eeboard.com/wp-content/uploads/downloads/2013/08/AR9331.pdf) with 16MB Flash and 64MB RAM running at 400MHz)

The MCU runs in *hard* real-time: you can use it to e.g. directly control servo motors or interface to sensors. The CPU on the other hand is powered by an embedded Linux ([Linino](https://github.com/arduino/linino)) that does not run in hard real-time, but is **capable of doing full flavored TCP/IP networking over Ethernet and Wifi**. The MCU and the CPU are connected via a serial interface.

The Yun's CPU and RAM are enough to run things like Node.js (but not much more). The biggest limitation are the 16MB flash, of which 8MB are reserved as a a recovery partition. We provide a tutorial for how to set up the Yun to use a microSD card for its filesystem.

## Connecting the Yun to the World

Now, while the Arduino Yun (like all Arduinos) already allows you to create awesome hardware oriented projects, wouldn't it be great if you could <span style="color: #ff6600; font-size: 110%;">connect your Arduino Yun to other devices, browsers or mobile apps, communicating in *(soft) real-time* over the Web?</span>

You can do so using [WAMP](http://wamp.ws/). Using WebSocket as a transport allows bidirectional real-time messaging on the Web and WAMP adds asynchronous [Remote Procedure Calls](http://wamp.ws/faq/#rpc) and [Publish & Subscribe](http://wamp.ws/faq/#pubsub) on top of WebSocket.

Here is an example of what you can do with Arduino Yun and WAMP:

 * stream sensor readings in real-time from the Arduino Yun via WebSocket to HTML5 browsers on desktop and mobile
 * control LEDs directly from your browser (again in real-time with very small latency)

{% if config.NONETWORK %}
   <center><br><br><b>YouTube video excluded in "no-network mode"!</b><br><br></center>
{% else %}
   <div class="videoBox">
      <iframe class="video" type="text/html" src="http://www.youtube.com/embed/Egvu4jL_Wlo?version=3&vq=hd720&frameborder=0&allowfullscreen&autohide=2&modestbranding=1&showinfo=0&rel=0&origin=http://tavendo.com" frameborder="0"/></iframe>
      <div class="videoCaption">Arduino Yun Real-time Charting over WebSocket with Autobahn</div>
   </div>   
{% endif %}

> The demo shows a shield on the Yun with 2 potis, 3 LEDs and 2 buttons, which are controlled from a simple sketch running on the Arduino. The sketch communicates over serial with Autobahn|Python running on the Linux side of the Yun, providing WAMP connectivity. And Autobahn in turn runs as a bridge that shuffles data from/to serial and to WebSocket/WAMP clients (here, Chrome running on desktop and on Nexus 4) connecting to Autobahn over Wifi.
> 

We'll give you step-by-step instructions for how to set up a Yun to work with WAMP. Specifically, we're going to set up Node.js and Autobahn|JS to enable you to access the Arduino pins on the Yun remotely (from any language with a WAMP implementation).

## Next steps

- [Basic setup]() 
- [Expanding disk space]()
- [installing node/autobahn/firmata for remote control]()