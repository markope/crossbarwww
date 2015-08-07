<div class="topimage_container">
   <img class="topimage" src="../../static/img/iotcookbook/yun_tutorial_hardware.jpg" alt="">   
</div>

This tutorial shows you how to connect the Arduino Yun to Crossbar.io. Having finished the tutorial will enable you to access the Yun from any WAMP application component.

The tutorial consists of three parts:

1. [Part 1](https://github.com/crossbario/crossbarexamples/tree/master/iotcookbook/device/yun/tutorial/tutorial1)
2. [Part 2](https://github.com/crossbario/crossbarexamples/tree/master/iotcookbook/device/yun/tutorial/tutorial2)
3. [Part 3](https://github.com/crossbario/crossbarexamples/tree/master/iotcookbook/device/yun/tutorial/tutorial3)

The **first part** only involves the Yun microcontroller running a simple firmware that reads a digital value from a button and an analog value from a potentiometer, and controls a LED depending on the former values.

<img src="../../static/img/iotcookbook/yun_tutorial_part1.jpg" alt="" />

The **second part** shows how to talk to the microcontroller from a Python program via serial. It still does not involve Crossbar.io or WAMP, but it is essential to let the Yun microcontroller talk to the outside world.

<img src="../../static/img/iotcookbook/yun_tutorial_part2.jpg" alt="" />

The **third part** now combines the knowledge from the previous parts and extends the Python program to act as a bridge between the serial connection (talking to the microcontroller) and a WAMP session (talking to Crossbar.io).

<img src="../../static/img/iotcookbook/yun_tutorial_part3.jpg" alt="" />
