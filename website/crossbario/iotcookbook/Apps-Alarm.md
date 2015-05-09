In this application, an alarm can be triggered by one or more accelerometers. The alarm is displayed in a browser frontend, of which any number of instances can be run concurrently.

Extensions to this are

* use a camera to take an image of the protected space on alarm, periodically or on user request (code for Tessel with camera module)
* play an alarm message to the intruder (code for speech synthesis on the Raspberry Pi)
* trigger alarm lights (code for the Arduino Yun and Raspberry Pi)
* hardware control for arming, disarming, manually triggering and stopping an alarm (code for the Arduino Yun and Raspberry Pi)

## The Basics

There is more than one way of running this application. Following are brief descriptions of the basic components required.

The technical requirements are:

* system with Crossbar.io + Node.js installed to run the backend
* system which can run a browser
* microcontroller with an accelerometer (code for Tessel and Arduino Yun provided)

### The Backend

The backend receives a live stream of accelerometer data and determines whether any changes here should trigger an alarm. This is based, among other things, on whether the alarm is currently armed. It centrally distributes alarm events and changes in the armed state to all frontends.

The backend as is is written for Node.js, but would be trivial to adapt for other languages with a WAMP library. 

With the default Crossbar.io configuration for this app, the backend is launched automatically by Crossbar.io.

### The Web Frontend

The Web frontend displays the current alarm state (armed or disarmed), as well as a triggered alarm. It allows arming, disarming, manually triggering an alarm, and stopping a triggered alarm. 

If a camera is connected to the alarm system, it also displays the photo taken once the alarm is triggered, and allows requesting an image at any time.

With the default Crossbar.io configuration for this app, the frontend is served by Crossbar.io.

### The Accelerometers

The accelerometer publishes its state. 

Code for two hardware platforms is currently provided, with code for both in the `accelerometer` directory of this app. In each case, transfer the code over to the device, with the accelerometer connected to it, and run it. More information can be found in the description of the respective component:

* [[Tessel Accelerometer]]
* [[Arduino Yun Accelerometer]]


### Launching it all

Launch Crossbar.io from the app directory. This also starts the backend and serves the frontend.

Start one or more microcontrollers with accelerometers.

Open the frontend in a browser (served at: `http://<IP-of-System-running-Crossbar.io>:8080).

Arm the alarm and move an accelerometer to test.



## The Extras

The alarm app can be easily extended with additional hardware. Two of these do not require any modificactions to the basic app code: the Alarm Lights and the Hardware Controls. These just use existing events and procedures which the browser frontend already utilizes.

The Photos and Robo-Voice require additional code, with the former also requiring an extension of the browser frontend.

### Alarm Lights

The Alarm Lights can be added using any microcontroller which can trigger LEDs or other lights based on WAMP messages. We currently offer this for the Arduino Yun and Raspberry Pi.

No changes to the backend are required when using Alarm Lights - they get triggered by the same alarm event that the frontend subscribes to.

### Hardware Controls

The Hardware Controls can be added using any microcontroller which can trigger LEDs or other lights based on WAMP messages, and receive trigger events from buttons. We currently offer code for this for the Arduino Yun and Raspberry Pi.

No changes to the backend are required when using Hardware Controls - they use the same events and procedures that the browser frontend does.


### Taking Photos

We currently offer code to use the camera module on the Tessel. This works, but the encoding of the image and its transfer are slow. The default resolution for testing this is therefore QQVGA (yes, this low). Regard this more as a proof-of-concept than anything else. But then, when you already have a Tessel with a camera module, it's at least something you can do with it!

The code you need to run on the Tessel with the camera module is in the `camera` directory. More information about this component and how to get it working can be found in the [component documentation](Tessel Camera).

When you use the camera module, then you need to 

* replace the standard backend code with `backend_camera.js` - best by editing the Crossbar.io config to run this,
* use `frontend_camera.hmtl` instead of `index.html`. This is served under `http://<IP-of-System-running-Crossbar.io>:8080/frontend_camera.html`, or you could rename the files.

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

> Note: If you want to use both a camera and speech synthesis, then you need to create your own `backend.js` for this. This is a simple copy & paste job - there are no conflicts when merging the code from `backend_camera.js` and `backend_speech.js`. As a frontend you can use `frontend_camera.js`, since the speech synthesis is just an additional output channel.
