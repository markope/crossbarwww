In this application, an alarm can be triggered by one or more accelerometers. The alarm is displayed in a browser frontend, of which any number of instances can be run concurrently.

<div class="topimage_container">
   <img class="topimage" src="../../static/img/iotcookbook/alarm_app.jpg" alt="">   
</div>

Extensions to this are

* use a camera to take an image of the protected space on alarm, periodically or on user request (code for Tessel with camera module or Raspberry Pi with a webcam)
* play an alarm message to the intruder (code for speech synthesis on the Raspberry Pi)
* hardware control for arming, disarming, manually triggering and stopping an alarm (code for the Arduino Yun and Raspberry Pi)

## The Basics

There is more than one way of running this application. Following are brief descriptions of the basic components required.

The technical requirements are:

* system with Crossbar.io + Node.js installed to run the backend
* system which can run a browser
* microcontroller with an accelerometer (code for Tessel and Arduino Yun provided)

### The Backend

The backend receives a live stream of accelerometer data when the alarm is armed and determines whether any changes here should trigger an alarm. It centrally distributes alarm events and changes in the armed state to all frontends.

The backend as is is written for Node.js, but would be trivial to adapt for other languages with a WAMP library. 

With the default Crossbar.io configuration for this app, the backend is launched automatically by Crossbar.io.

### The Web Frontend

The Web frontend displays the current alarm state (armed or disarmed), as well as a triggered alarm. It allows arming, disarming, manually triggering an alarm, and stopping a triggered alarm. 

If a camera is connected to the alarm system, it also displays the photo taken once the alarm is triggered, and allows requesting an image at any time.

With the default Crossbar.io configuration for this app, the frontend is served by Crossbar.io.

### The Accelerometers

The accelerometer publishes its state. 

Code for two hardware platforms is currently provided, with code for both in the `accelerometer` directory of this app. In each case, transfer the code over to the device, with the accelerometer connected to it, and run it. More information about any additional setup which may be required can be found in the description of the respective component:

* [[Tessel Accelerometer]]
* [[Arduino Yun Accelerometer]]

<figure>
   <img src="/static/img/iotcookbook/alarmapp/accelerometer_tessel.jpg" alt="alarm app accelerometer - Tessel" class="imgCentered">
   <figcaption>Tessel with accelerometer module</figcaption>
</figure>


### Launching it all

Launch Crossbar.io from the app directory. This also starts the backend and serves the frontend.

```shell
crossbar start
```

Start one or more microcontrollers with accelerometers.

Open the frontend in a browser (served at: `http://<IP-of-System-running-Crossbar.io>:8080).

Arm the alarm and move an accelerometer to test.




## The Extras

The alarm app can be easily extended with additional hardware. One of these does not require any modificactions to the basic app code: the Hardware Controls. This just uses existing events and procedures which the browser frontend already utilizes.

The Photos and Robo-Voice require additional code, with the former also requiring an extension of the browser frontend.

### Hardware Controls

The Hardware Controls can be added using any microcontroller which can trigger LEDs or other lights based on WAMP messages, and receive trigger events from buttons. We currently offer code for this for the Arduino Yun.

No changes to the backend are required when using Hardware Controls - they use the same events and procedures that the browser frontend does.

<figure>
   <img src="/static/img/iotcookbook/alarmapp/hardware_controls_yun.jpg" alt="alarm app hardware controls on a yun with Tinkerkit" class="imgCentered">
   <figcaption>Yun with Tinkerkit controls</figcaption>
</figure>

The hardware requirements on the Yun are two Tinkerkit buttons and two Tinkerkit LEDs. The buttons need to be connected to pin 0 (arm/disarm the alarm) and 1 (trigger/cancel the alarm). The LEDS need to be connected to pin 11 (armed state indicator) and pin 10 (alarm state indicator).

You need to set up the Yun for [remote GPIO access](Arduino Yun Remote GPIO). Instead of the generic library provided there, use `hardware_controls_yun.js` in the `hardware_controls` folder.

Once you have your hardware connected, run the script

```shell
node hardware_controls_yun.js
```

which should log

```shell
Alarm App - Arduino Yun Hardware Controls starting ...
Arduino connected (over /dev/ttyATH0, board version 2.3)
Connecting to router ...
Router connected. Session ID: 196598121
```

### Taking Photos

We currently offer code to use the camera module on the Tessel and a webcam connected to the Pi. 

When you use a camera module you need to 

* replace the standard backend code with `backend_camera.js` - best by editing the Crossbar.io config to run this,
* use `frontend_camera.hmtl` instead of `index.html`. This is served under `http://<IP-of-System-running-Crossbar.io>:8080/frontend_camera.html` (or you could rename the files).

#### Tessel

The Tessel camera module somewhat works, but the encoding of the image and its transfer are slow. The default resolution for testing this is therefore QQVGA (yes, this low, but try how long a VGA image takes!). Regard this more as a proof-of-concept than anything else. But then, when you already have a Tessel with a camera module, it's at least something you can do with it!

The code you need to run on the Tessel with the camera module is in the `camera` directory - `camera_tessel.js`. More information about this component and how to get it working can be found in the [component documentation](Tessel Camera).

#### Raspberry Pi

The Pi supports most webcams, and works much faster than the Tessel.

The code you need is `camera_pi.js`. For instructions on how to get this working in general see the [Pi Camera Component documentation](Raspberry Pi Camera).


### Robo-Voice the Intruder

We currently offer code for a text-to-speech message using the Raspberry Pi.

The code you need to run the Raspberry Pi is in the `speech` directory. More information about how to set up this component can be found in the [component documentation](Raspberry Pi Speech Synthesis).

The short version: 

* get `speechsynt_adapter.py` onto the Pi (e.g. `scp speechsynth_adapter.py pi@<IP of your Pi>:~/`)
* start `speechsynth_adapter.py` by doing
```
python speechsynth_adapter.py --router 'ws://192.168.1.134:8080/ws' --realm 'iot_cookbook'
```

When you use this extra, you also need to replace the standard backend code with `backend_speech.js` - best by editing the Crossbar.io config to run this. Within this file, you need to set the correct ID for the Raspberry Pi you are using (search for  `piSerial` and replace the value with the device ID of your Pi). 

You may additionally want to adapt the text which is spoken (`alertText`) and the number of times this is repeated (`repetitions`).

> Note: If you want to use both a camera and speech synthesis, then you should use `backend_complete.js` and the camera frontend.
