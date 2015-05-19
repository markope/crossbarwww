## for WAMP and Crossbar.io




<div class="cookbook_topbox_landingpage">
   <div id="cookbook_home_topimage_container">
      <img id="cookbook_home_topimage" src="../static/img/iotcookbook/lego_duplo_smaller.jpg" alt="">   
   </div>
   
   <h2>
      You want to solve a problem - we offer components and recipes to build your solutions
   </h2>

   <ul>
      <li>
         All components come with <strong>built-in connectivity</strong>. They can connect from anywhere,  and you can easily  build distributed applications.
      </li>
      <li>
         All components can <strong>communicate freely with each other</strong> - including calling procedures. The compoments connect via a Crossbar.io application router. Client libraries for WAMP, the protocol used, are available for 9 languages (and growing). You can also integrate services with REST APIs, so your applications can talk to pretty much anything on the internet.
      </li>
      <li>
         All recipes include <strong>step-by-step instructions</strong> to get things working. Just follow the instructions - no need to worry about the technological background details. If you want to dive deeper into the technology, we provide links to get your started.
      </li>
      <li>
         The software used in these recipes is <strong>open source</strong>, and part of a growing ecosystem aorund the WAMP protocol.
      </li>
      <li>
         A <strong>variety of microcontrollers</strong>, including the Raspberry Pi and Arduino Yun, are used as part of components.
      </li>
   </ul>
</div>

## The components

Building blocks, ready to use for solving your problem!



* Speech Synthesis [Raspberry Pi](Raspberry Pi Speech Synthesis)
* X-Box Controller [Raspberry Pi](Raspberry Pi Xbox Controller)
* Accelerometer [Tessel](Tessel Accelerometer)/[Yun](Arduino Yun Accelerometer)
* Lights [Yun](Arduino Yun Lights)
* Camera [Tessel](Tessel Camera)/[Raspberry Pi](Raspberry Pi Camera)
* Buttons [Yun](Arduino Yun Buttons)

* [Digital Signage](Digital Signage):
   
   + [Browser Remote Control](Browser Remote Control)
   + [Reveal.js Remote Control](Reveal.js Remote Control)
   + [WAMP widgets](WAMP Browser Widgets) (**under construction**)

plus generic remote access & control of GPIO pins on the

* [Arduino Yun](Arduino Yun Remote GPIO)
* [Raspberry Pi](Raspberry Pi Remote GPIO) (**under construction**)

## The applications

Applications which use the components. Get an idea for how combining things works, find code to re-use, be inspired - and maybe already find a solution which fits your needs!

* [Alarm Application](Apps Alarm)
* [Real-time charting with the Arduino Yun](Arduino Yun Real-time Charting) (**under construction**)
* [Digital Signage](Digital Signage)
  
## Components and applications by device

Pick a microcontroller and see what we are offering for it: 

* [[Raspberry Pi]]
* [[Arduino Yun]]
* [[Tessel]]


## Running things

The code for all of the above is in the [crossbarexamples repository](https://github.com/crossbario/crossbarexamples) under `iotcookbook`. Clone this locally or download it as a ZIP file.

## Getting a WAMP router

There are three main ways to gettin a WAMP router

* We offer a [demo instance](../docs/Demo-Instance) (**under construction**) for testing and light development workloads.
* You can quickly spin up a virtual machine with Crossbar.io preinstalled. We suggest [Microsoft Azure](../docs/Setup-on-Microsoft-Azure), but [Amazon EC2](../docs/Setup-on-Amazon-EC2) also works.
* You can [install Crossbar.io yourself](../docs/Local-Installation).


