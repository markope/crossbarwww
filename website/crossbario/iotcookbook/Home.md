## for WAMP and Crossbar.io

## You want to solve a problem - we offer components and recipes to build your solutions

* All components come with **built-in connectivity**. They can connect from anywhere,  and you can easily  build distributed applications.

* All components can **communicate freely with each other** - including calling procedures. The compoments connect via a Crossbar.io application router. Client libraries for WAMP, the protocol used, are available for 9 languages (and growing). You can also integrate services with REST APIs, so your applications can talk to pretty much anything on the internet.
           
* All recipes include **step-by-step instructions** to get things working. Just follow the instructions - no need to worry about the technological background details. If you want to dive deeper into the technology, we provide links to get your started.

* The software used in these recipes is **open source**, and part of a growing ecosystem aorund the WAMP protocol.

* A **variety of microcontrollers**, including the Raspberry Pi and Arduino Yun, are used as part of components.

## The components

Building blocks, ready to use for solving your problem!

* [Speech Synthesis (Raspberry Pi)](Raspberry Pi Speech Synthesis)
* [X-Box Controller (Raspberry Pi)](Raspberry Pi Xbox Controller)
* Accelerometer [Tessel](Tessel Accelerometer)/[Yun](Arduino Yun Accelerometer)
* Lights [Yun](Arduino Yun Lights)
* Camera [Tessel](Tessel Camera)/[Raspberry Pi](Raspberry Pi Camera)

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


