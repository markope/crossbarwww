Send events from an Xbox controller connected to a Pi to WAMP components anywhere.

## Try it out

The code for the example consists of a adapter written in Python and AutobahnPython using Twisted. The adapter runs on the Pi and connects to Crossbar.io running on a network accessible from the Pi.

Included is a frontend running in the browser. The frontend is written in JavaScript using AutobahnJS and connects to the same Crossbar.io router instance as the adapter connects to. Consequently, the frontend is able to invoke the procedures exposed on the Pi and subscribe to events generated from there.

## Preparations on the Pi

Install [xboxdrv](https://github.com/xboxdrv/xboxdrv) (a userspace drive for Xbox gamepad controllers):

```console
sudo apt-get install -y xboxdrv
```

Test the driver:

```console
pi@raspberrypi ~/scm/crossbarexamples/device/pi/xboxcontroller $ sudo xboxdrv --quiet --detach-kernel-driver
```

which should give you output like this:

```console
X1:  1126 Y1:  4564  X2:  1933 Y2:  3268  du:0 dd:0 dl:0 dr:0  back:0 guide:0 start:0  TL:0 TR:0  A:0 B:0 X:0 Y:0  LB:0 RB:0  LT:  0 RT:  0
X1:  1126 Y1:  4564  X2:  1933 Y2:  3646  du:0 dd:0 dl:0 dr:0  back:0 guide:0 start:0  TL:0 TR:0  A:0 B:0 X:0 Y:0  LB:0 RB:0  LT:  0 RT:  0
X1:  1126 Y1:  4564  X2:  1933 Y2:  4024  du:0 dd:0 dl:0 dr:0  back:0 guide:0 start:0  TL:0 TR:0  A:0 B:0 X:0 Y:0  LB:0 RB:0  LT:  0 RT:  0
X1:  1126 Y1:  4564  X2:  1933 Y2:  4402  du:0 dd:0 dl:0 dr:0  back:0 guide:0 start:0  TL:0 TR:0  A:0 B:0 X:0 Y:0  LB:0 RB:0  LT:  0 RT:  0
X1:  1126 Y1:  4564  X2:  1546 Y2:  4780  du:0 dd:0 dl:0 dr:0  back:0 guide:0 start:0  TL:0 TR:0  A:0 B:0 X:0 Y:0  LB:0 RB:0  LT:  0 RT:  0
X1:  1126 Y1:  4564  X2:  1546 Y2:  5158  du:0 dd:0 dl:0 dr:0  back:0 guide:0 start:0  TL:0 TR:0  A:0 B:0 X:0 Y:0  LB:0 RB:0  LT:  0 RT:  0
X1:  1126 Y1:  4564  X2:  1159 Y2:  5914  du:0 dd:0 dl:0 dr:0  back:0 guide:0 start:0  TL:0 TR:0  A:0 B:0 X:0 Y:0  LB:0 RB:0  LT:  0 RT:  0
X1:  1126 Y1:  4564  X2:   772 Y2:  5914  du:0 dd:0 dl:0 dr:0  back:0 guide:0 start:0  TL:0 TR:0  A:0 B:0 X:0 Y:0  LB:0 RB:0  LT:  0 RT:  0
X1:  1126 Y1:  4564  X2:   772 Y2:  6292  du:0 dd:0 dl:0 dr:0  back:0 guide:0 start:0  TL:0 TR:0  A:0 B:0 X:0 Y:0  LB:0 RB:0  LT:  0 RT:  0
X1:  1126 Y1:  4564  X2:   256 Y2:  6292  du:0 dd:0 dl:0 dr:0  back:0 guide:0 start:0  TL:0 TR:0  A:0 B:0 X:0 Y:0  LB:0 RB:0  LT:  0 RT:  0
X1:  1126 Y1:  4564  X2:   256 Y2:  6796  du:0 dd:0 dl:0 dr:0  back:0 guide:0 start:0  TL:0 TR:0  A:0 B:0 X:0 Y:0  LB:0 RB:0  LT:  0 RT:  0
X1:  1126 Y1:  4564  X2:  -131 Y2:  6796  du:0 dd:0 dl:0 dr:0  back:0 guide:0 start:0  TL:0 TR:0  A:0 B:0 X:0 Y:0  LB:0 RB:0  LT:  0 RT:  0
X1:  1126 Y1:  4564  X2:  -131 Y2:  6292  du:0 dd:0 dl:0 dr:0  back:0 guide:0 start:0  TL:0 TR:0  A:0 B:0 X:0 Y:0  LB:0 RB:0  LT:  0 RT:  0
X1:  1126 Y1:  4564  X2:  -131 Y2:  5788  du:0 dd:0 dl:0 dr:0  back:0 guide:0 start:0  TL:0 TR:0  A:0 B:0 X:0 Y:0  LB:0 RB:0  LT:  0 RT:  0
...
```

Install Autobahn|Python

```console
sudo pip install autobahn
```

## Running the example

You need a Crossbar.io instance for the Xbox Controller adapter on the Pi and the browser frontend to connect to.

The simplest way is to navigate to `iotcookbook/device/pi/xboxcontroller` in your local `crossbarexamples` repo, and do

```console
crossbar start
```

This will also serve the browser frontend under

```
http://localhost:8080/xboxcontroller_frontend.html
```

Get `xboxcontroller_adapter.py` onto the Pi and then start it, passing the URL of Crossbar.io and the realm to connect to

```console
sudo xboxdrv --quiet --detach-kernel-driver | python xboxcontroller_adapter.py --router ws://192.168.1.134:8080/ws
```


## The API

`xboxcontroller_adapter` exposes one procedure

```
io.crossbar.examples.iot.devices.pi.<DEVICE_ID>.xboxcontroller.get_data
``` 

which returns the present state of the controller,

and publishes events to one topic

```
io.crossbar.examples.iot.devices.pi.<DEVICE_ID>.xboxcontroller.on_data
```

which yields a continuous stream of controller data.

The controller data itself is sent as JSON, and you can extract relevant events from this.

## Using it

