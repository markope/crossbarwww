Output (English) sentences from your Pi which are sent as text via WAMP.

The example uses the [flite](http://www.festvox.org/flite/) text-to-speech engine to convert english sentences to voice which is then output via the Pi's audio output.


## Try it out

The code for the example consists of an adapter written in Python and AutobahnPython using Twisted. The adapter runs on the Pi and connects to Crossbar.io running on a network accessible from the Pi.

Included is a frontend running in the browser. The frontend is written in JavaScript using AutobahnJS and connects to the same Crossbar.io router instance as the adapter connects to. Consequently, the frontend is able to invoke the procedures exposed on the Pi and subscribe to events generated from there.

### Preparations on the Pi

[Enable audio](https://www.raspberrypi.org/documentation/configuration/audio-config.md) output on the 3.5mm plug:

```console
sudo amixer cset numid=3 1
```

Install the [flite](http://www.festvox.org/flite/) text-to-speech processor:

```console
sudo apt-get install -y flite
```

Test the text-to-speech engine:

```console
flite -voice slt "Hi, my name is Susan. How can I help you?"
```

The volume may be a bit low. To increase that to (near) the maximum, do

```shell
sudo amixer set PCM -- -100
```

You can, of course, increase the volume less by choosing a higher value than `-100`.

Install Autobahn|Python

```console
sudo pip install autobahn
```

### Running the Speech Synthesis

The code for this can be found in the [crossbarexamples GitHub repository](https://github.com/crossbario/crossbarexamples) under `iotcookbook`. You need to clone this (or [download it as a ZIP file](https://github.com/crossbario/crossbarexamples/archive/master.zip)).

You need a Crossbar.io instance for the Speech Synthesis adapter on the Pi and the browser frontend to connect to.

The simplest way is to navigate to `iotcookbook/device/pi/speechsynt` in your local `crossbarexamples` repo, and do

```console
crossbar start
```

This will also serve the browser frontend under

```
http://localhost:8080/speechsynth_frontend.html
```

Get `speechsynth_adapter.py` onto the Pi, e.g. via scp

```console
scp speechsynth_adapter.py pi@<IP of your Pi>:~/
```

and then start it, passing the URL of Crossbar.io and the realm to connect to, e.g.

```console
python speechsynth_adapter.py --router 'ws://192.168.1.134:8080/ws' --realm 'iot_cookbook'
```

Then use the browser frontend to send a text of your choice. (Be aware that the full text you send is rendered to audio before playback starts. Long texts can take a while to start - so better to chunk them into smaller bits.)


## The API

The adapter exposes these procedures

* `io.crossbar.examples.iot.devices.pi.<DEVICE ID>.speechsynth.say` - takes a string as argument ([string]). Returns once the text has been processed and spoken. Fails if text is currently being spoken (so check first using the procedure below).

* `io.crossbar.examples.iot.devices.pi.<DEVICE ID>.speechsynth.is_busy` - returns true if a text is presently being spoken or processed. 

and publishes event to these topics

* `io.crossbar.examples.iot.devices.pi.<DEVICE ID>.speechsynth.on_ready` - sent once the component is initialized
* `io.crossbar.examples.iot.devices.pi.<DEVICE ID>.speechsynth.on_speech_start` - sent when the processing of received text has started
* `io.crossbar.examples.iot.devices.pi.<DEVICE ID>.speechsynth.on_speech_end` - sent when the processing and output of speech has finished.


## Using it

No real difference to the trying out - run 'speechsynth_adapter.py' on the Pi, connect to a WAMP router, call from any WAMP component using the above API.