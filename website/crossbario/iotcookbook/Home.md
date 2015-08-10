<div id="iotcookbook_introblock">
   <div>
      The <strong>IoT Cookbook</strong> provides a collection of ready-to-build recipes for connected IoT components to create your next IoT application.<br>

      <iframe allowtransparency="true" frameborder="0" scrolling="no" src="https://platform.twitter.com/widgets/tweet_button.html?url=http://crossbar.io/iotcookbook/&via=crossbario&count=none&hashtags=iot,wamp,crossbar&text=IoT Cookbook: ready-to-build, open-source recipes for connected IoT components" style="width:70px; height:20px;"></iframe>
   </div>
</div>

<p style="margin-top: 20px;">
   The <strong>IoT Cookbook</strong> provides a collection of ready-to-build recipes for connected IoT components to create your next IoT application.
</p>
<p>
   Building on tested and documented components, makers and developers get a head start and can focus on creating their actual application functionality.
</p>

<p class="note">
<b>NEWS, 2015/08/08:</b> We've streamlined the Getting Started pages for all devices, in particular the Yun is now much simpler to setup. And we've released first pages for the Intel Edison
</p>
<br>

<b>Quick access by device type:</b>

All recipes and documentation in the IoT Cookbook can be accessed starting from one of the covered devices. The devices we currently cover in the IoT Cookbook are:
<br><br>

<div id="devices_quick_access">
   <a href="Arduino-Yun">
      <div class="device">
         Arduino Yun (MIPS)<br>
         <img class="cookbook_home_device" src="../static/img/iotcookbook/arduino_yun.jpg" alt="">
      </div>
   </a>
   <a href="Intel-Edison">
      <div class="device">
            Intel Edison (x86)<br>
            <img class="cookbook_home_device" src="../static/img/iotcookbook/edison/edison.jpg" alt="" >
      </div>
   </a>
   <a href="Raspberry-Pi">
      <div class="device">
            Raspberry Pi (ARM)<br>
            <img class="cookbook_home_device" src="../static/img/iotcookbook/raspberry_pi.jpg" alt="">
      </div>
   </a>
   <a href="Tessel">
      <div class="device">
            Tessel (MIPS)<br>
            <img class="cookbook_home_device" src="../static/img/iotcookbook/tessel.jpg" alt="" >
      </div>
   </a>
</div>

<div style="clear: both; height: 0;">&nbsp;</div>

<p class="note">
<b>Note:</b>
If you find errors, bugs or other issues in above, or if you have new contributions (awesome!!), we would be happy to receive your <a href="https://github.com/crossbario/crossbarwww">feedback or PRs on GitHub</a>!
</p>

<br>


# Overview

<div class="cookbook_topbox_landingpage">
   <p>
      <b>You want to solve a problem and focus your efforts at the application level</b>, not fiddle around to get some basic IoT sensor or actuator component built and connected to your application backends.
   </p>
   <p>
      With the component collection and all the recipes and tutorials, the IoT Cookbook wants to <b>free you from having to reinvent the wheels all over again</b>.
   </p>
<p>
   Components are connected using <strong>Crossbar.io</strong>, which
   allows you to <strong>communicate with WAMP-enabled IoT devices</strong> from more than <strong><a href="http://wamp.ws/implementations/#libraries">9 programming languages</a></strong>. The IoT Cookbook has material for different languages as well. And we show how to build your own, reusable components, giving you the ultimate control.
</p>
   <br>
   <ul>
      <li>
         All components come with <strong>built-in connectivity</strong>. They can connect from anywhere, and you can easily build distributed applications.
      </li>
      <li>
         All components can <strong>communicate freely with each other</strong> - including calling procedures. The components connect via a Crossbar.io application router. Client libraries for WAMP, the protocol used, are available for <strong><a href="http://wamp.ws/implementations/#libraries">9 languages</a></strong> (and growing). You can also integrate services with REST APIs, so your applications can talk to pretty much anything on the internet.
      </li>
      <li>
         All recipes include <strong>step-by-step instructions</strong> to get things working. Just follow the instructions - no need to worry about the technological background details. If you want to dive deeper into the technology, we provide links to get your started.
      </li>
      <li>
         The software used in these recipes is <strong>open source</strong>, and part of a growing ecosystem around the WAMP protocol.
      </li>
      <li>
         A <strong>variety of microcontrollers</strong>, including the Raspberry Pi and Arduino Yun, are used as part of components.
      </li>
   </ul>
</div>


# Running things

All the code and examples from the IoT Cookbook is on GitHub **[here](https://github.com/crossbario/crossbarexamples/iotcookbook)**. Clone this locally or [download](https://github.com/crossbario/crossbarexamples/archive/master.zip) it as a ZIP archive.

Most of the examples in the IoT Cookbook **require a WAMP router** for communication between WAMP-enabled IoT devices and other application components. While you can use [any WAMP router](http://wamp.ws/implementations/#routers), we recommend Crossbar.io.

Here are your options:

**Option 1**: Use our hosted [Crossbar.io demo instance](../docs/Demo-Instance) for testing and light development

**Option 2**: Spin up your own VM with [Crossbar.io on Microsoft Azure](../docs/Setup-on-Microsoft-Azure)

<!--
<a href="http://azure.microsoft.com/en-us/marketplace/partners/tavendo/crossbar-on-azure-ubuntu1404/">
   <img src="../static/img/iotcookbook/crossbar_sample_533x324.png" alt="" style="box-shadow: none; border: none;" />
</a>
-->

**Option 3**: Spin up your own VM with [Crossbar.io on Amazon EC2](../docs/Setup-on-Amazon-EC2)

**Option 4**: Install and [run Crossbar.io locally](../docs/Local-Installation)


# Devices

Pick a device and see what we are offering for it:

* [[Raspberry Pi]]
* [[Arduino Yun]]
* [[Tessel]]
* [[Intel Edison]]

# Components

IoT building blocks, ready to use in your application:

* Sensors
   * Accelerometer - [Tessel](Tessel Accelerometer)/[Yun](Arduino Yun Accelerometer)
   * Ambient Light - [Yun](Arduino Yun Ambient Light Sensor)
   * Camera - [Tessel](Tessel Camera)/[Raspberry Pi](Raspberry Pi Camera)
   * Tilt Sensor - [Yun](Arduino Yun Tilt Sensor)
   * [Raspberry Pi Temperature Monitor](Raspberry Pi Temperature Monitor)
   * Weighing Pad - [Yun](Arduino Yun Weighing Pad)
* Inputs
   * X-Box Controller -[Raspberry Pi](Raspberry Pi Xbox Controller)
   * Buttons - [Yun](Arduino Yun Buttons)
   * Potentiometer - [Yun](Arduino Yun Potentiometer)
   * Novation Launchpad - [Raspberry Pi](Raspberry Pi Novation Launchpad) (**under construction**)
* Outputs
   * Speech Synthesis - [Raspberry Pi](Raspberry Pi Speech Synthesis)
   * Sample Playback -[Raspberry Pi](Raspberry Pi Sample Player)
   * Lights - [Yun](Arduino Yun Lights)
   * [LED Matrix Display](Arduino Yun LED Matrix Display)
   + [Browser Remote Control](Browser Remote Control)
   + [Reveal.js Remote Control](Reveal.js Remote Control)
   + [WAMP widgets](WAMP Browser Widgets) (**under construction**)

plus generic remote access & control of GPIO pins on the

* [Arduino Yun](Arduino Yun Serial to WAMP Bridge)
* [Raspberry Pi](Raspberry Pi Remote GPIO) (**under construction**)


# Applications

Applications which use the components. Get an idea for how combining things works, find code to re-use, be inspired - and maybe already find a solution which fits your needs!

* [Alarm Application](Apps Alarm)
* [Digital Signage](Digital Signage)
* [Euro Pallet Load](Euro Pallet Load)
* [Real-time charting with the Arduino Yun](Arduino Yun Real-time Charting) (**under construction**)
