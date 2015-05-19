<div class="topimage_container">
   <img class="topimage" src="../../static/img/iotcookbook/digital_signage.jpg" alt="">   
</div>


## What this is about

'Digital Signage' refers to using digital displays instead of printer materials, neon etc. as signs. This becomes especially useful with the possibility to update or control the content remotely.

Digital Signage can be an end in itself (which is why it's linked to under 'Apps'), or form part of a larger application (thus the link from 'Components' ).

We describe how to create your own digital signage solutions using open source software and cheap, off-the-shelf hardware.

The command & control channel to the digital signs is created using WAMP & Crossbar.io.

## Hardware Requirements

The solutions we describe here are all browser based. This means that, in principle, you can implement them using any device which

* runs a modern Web browser
* has an Internet connection

The components generally make no more assumptions than this.

We think that currently the Raspberry Pi 2 is a good driver for digital signage. It is inexpensive, has an HDMI output and enough processing power to run standard Web pages. We include a How-To for setting up the Pi for digital signage.


## The Components

### Controlling the browser

The [browserremote](Browser Remote Control) component can be embedded in any Web page whose source code you can modify. As such you can use WAMP events to

* reload the page (e.g. when the content has changed)
* navigate to another page
* open up an additional tab and control the page this displays.

* [browserremote](Browser Remote Control)

### Controlling a presentation

[Reveal.js](https://github.com/hakimel/reveal.js/) is probably the most well-established library for HTML5 presentations. It allows for presentations with impressive graphical effects out of the box, and you can extend presentations to use the full power of modern browsers.

Using the [revealremote](Reveal.js Remote Control) component, you can remote control your Reveal.js presentations via WAMP. Just include two JavaScript files, and you can navigate presentations or set auto-play from any WAMP application. The component includes a simple browser frontend to get you started.

* [revealremote](Reveal.js Remote Control)

### ... on as many displays as you like

An advantage of both the browserremote and revealremote components is that you can control as many displays as you want simultaneously. Running a wall of displays in sync is as easy as controlling a single one!


### Displaying live data

**-- under construction! ---**

With WAMP its also very easy to display live data streams. New information can be pushed to the browser, allowing low-latency updates.

The widgets listed below are there to get you started. They provide some basic forms of information visualization, and show how updating information via WAMP is handled.

If you want more types of visualization, more graphically appealing widgets, or you simply alredy have a widget set: It should be easy to adapt most modern HTML5 widget sets based on the mechanisms our code illustrates.

* [Widgets overview]()
* [Simple Text Widget]()
* [Single Bar Widget]()
* [Bar Chart Widget]()
* [Pie Chart Widget]()
* [Stock Price Widget]()

## Setting up a Raspberry Pi

At a retail price of around 30 euros, and with a huge developer community around it, the Raspberry Pi 2 is a perfect candidate for controlling digital signage. 

We have a [tutorial](Raspberry Pi Digital Signage Setup) which shows you how to set up a Raspberry Pi so that it boots into a browser and loads a pre-configured page. This means that all you need to do is to clone the basic setup when you've done it and then copy it to an SD card for each new Pi you want to add. 

