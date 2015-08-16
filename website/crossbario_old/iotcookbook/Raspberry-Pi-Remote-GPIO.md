**-- under construction --**

The example shows how to expose two LEDs and a button wired to the Pi's [GPIOs](https://www.raspberrypi.org/documentation/usage/gpio/) via WAMP so you can turn on/off the LEDs and sense the button from **any other** WAMP component.


## Try it out

The code for the example consists of a adapter written in Python and AutobahnPython using Twisted. The adapter runs on the Pi and connects to Crossbar.io running on a network accessible from the Pi.

Comes with a frontend running in browsers. The frontend is written in JavaScript using AutobahnJS and connects to the same Crossbar.io router instance as the backend connects to. Consequently, the frontend is able to invoke the procedures exposed on the Pi and subscribe to events generated from there.

### The hardware side



### The software side

The code for this can be found in the [crossbarexamples GitHub repository](https://github.com/crossbario/crossbarexamples) under `iotcookbook`. You need to clone this (or [download it as a ZIP file](https://github.com/crossbario/crossbarexamples/archive/master.zip)).

If you don't have aleady, login to your Pi and install Autobahn:

```console
sudo pip install autobahn
```

> If you run a recent Raspbian, you are all set. If not, you might need to install [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO) `sudo apt-get install python-dev python-rpi.gpio`


Copy the backend component from your computer to the Pi:

```console
scp gpio_backend.py pi@<IP of your Pi>:~/
```

and login to start the component

```
sudo python gpio_adapter.py --router <WebSocket URL of your Crossbar.io Router>
```

> The backend has to run as root because it needs to access the GPIOs, which is a restricted operation. 

## The API

The adapter exposes these procedures

* `io.crossbar.examples.iot.devices.pi.<DEVICE ID>.gpio.set_digout`
* `io.crossbar.examples.iot.devices.pi.<DEVICE ID>.gpio.get_digout`
* `io.crossbar.examples.iot.devices.pi.<DEVICE ID>.gpio.toggle_digout`
* `io.crossbar.examples.iot.devices.pi.<DEVICE ID>.gpio.get_digin`

and publishes event on these topics

* `io.crossbar.examples.iot.devices.pi.<DEVICE ID>.gpio.on_ready`
* `io.crossbar.examples.iot.devices.pi.<DEVICE ID>.gpio.on_digout`
* `io.crossbar.examples.iot.devices.pi.<DEVICE ID>.gpio.on_digin`

## Using it





## Links

* http://pi.gadgetoid.com/pinout
* http://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/
* https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/install-python-module-rpi-dot-gpio




