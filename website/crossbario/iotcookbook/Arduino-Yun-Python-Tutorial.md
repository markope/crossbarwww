<div class="topimage_container">
   <img class="topimage" src="../../static/img/iotcookbook/yun_tutorial_hardware.jpg" alt="">
</div>

This tutorial shows you the basics of programming the Yun, as well as how to connect the Arduino Yun to Crossbar.io. Having finished the tutorial will enable you to access the Yun from any WAMP application component, and give you a start in programming your own components.

We'll show you how to run code within the the Arduino MCU on the Yun, how to communication between the MCU and the Linux system works, and how to connect the Linux system as part of a WAMP application.

This is the Python version of this tutorial. There is also a [JavaScript/Node.js version](Arduino Yun JavaScript Tutorial) if you feel more comfortable with this.

## Prerequisites

You need to have a basic understanding of Python, and some knowledge of C would be good (though you can probably do some basic hacking of the C code for the MCU without that).

If you want to run the example code, you should also have an Arduino Yun set up to run AutobahnPython - see either the [Quick Setup](Arduino Yun Quick Setup) or the [Detailed Setup](Arduino Yun Detailed Setup). You also need a button, a potentiometer and a LED connected to the Yun (though you can substitute other input & output devices).

## The tutorial

The tutorial consists of three parts. The code for the parts is on GitHub:

1. [Part One](https://github.com/crossbario/crossbarexamples/tree/master/iotcookbook/device/yun/tutorial/tutorial1)
2. [Part Two](https://github.com/crossbario/crossbarexamples/tree/master/iotcookbook/device/yun/tutorial/tutorial2)
3. [Part Three](https://github.com/crossbario/crossbarexamples/tree/master/iotcookbook/device/yun/tutorial/tutorial3)

### Part One

Tutorial [Part One](https://github.com/crossbario/crossbarexamples/tree/master/iotcookbook/device/yun/tutorial/tutorial1) only involves the Yun microcontroller running a simple firmware that reads a digital value from a button and an analog value from a potentiometer, and turns on the LED if either the button is pressed or the potentiometer is turned beyond a certain threshold. The system in this case looks like

<img src="../../static/img/iotcookbook/yun_tutorial_part1.jpg" alt="" />

To run the the code for the first part:

* download it to your dev machine,
* connect the dev machine to the Yun via USB,
* run the Arduino IDE and select your Yun
* compile & upload the downloaded code to the Yun

### Part Two

Tutorial [Part Two](https://github.com/crossbario/crossbarexamples/tree/master/iotcookbook/device/yun/tutorial/tutorial2) shows how to talk to the microcontroller from a Python program via serial. It still does not involve Crossbar.io or WAMP, but it is essential to let the Yun microcontroller talk to the outside world.

Here the code on for the MCU reads the digital value from the button and the analog value from the potentiomenter and writes these to the serial port. The Python code on the Linux system reads the serial port, decides what the LED state should be based on the received values, and then writes the button state on the serial port. The code uses Twisted, a Pyhton framework for asynchronous programming, which is used by AutobahnPython and Crossbar.io. In this case the system looks like:

<img src="../../static/img/iotcookbook/yun_tutorial_part2.jpg" alt="" />

Tun run the code for the second part:

* for the code for the MCU, follow the instructions for the first part
* download the Pyhton code
* transfer this to the Linux part of the Yun, e.g. using SSH

```shell
scp controller.py root@192.168.1.141:~/ 
```

### Part Three

Tutorial [Part Three](https://github.com/crossbario/crossbarexamples/tree/master/iotcookbook/device/yun/tutorial/tutorial3) now combines the knowledge from the previous parts and extends the Python program to act as a bridge between the serial connection (talking to the microcontroller) and a WAMP session (talking to Crossbar.io). The system here looks like this

<img src="../../static/img/iotcookbook/yun_tutorial_part3.jpg" alt="" />

You can run Crossbar.io with a working configuration from the tutorial base directory by doing

```
crossbar start
```

This serves the frontend at `http://localhost:8080`. Open the JavaScript console to see received values, click on the buttons to toggle the LED on the Yun. 

The bridge component provides a couple of procedures ("get_sensors", "set_led"), and publishes the current data. Here you need to modify the code with the IP of the computer that you run Crossbar.io on.

Otherwise the code for the third part can be run just like the code for the second part (just switch the files you use).
