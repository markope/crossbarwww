Trigger samples stored on your Pi via WAMP messages, add samples via URL.

<div class="topimage_container">
   <img class="topimage" src="../../static/img/iotcookbook/speech_raspberry_pi.jpg" alt="">   
</div>

The example uses the [pygame library mixer](https://www.pygame.org/docs/ref/mixer.html) to play samples stored on the Pi in WAV or OGG format.

## Try it out

The code for the example consists of an adapter written in Python and AutobahnPython using Twisted. The adapter runs on the Pi and connects to Crossbar.io running on a network accessible from the Pi.

Included is a frontend running in the browser. The frontend is written in JavaScript using AutobahnJS and connects to the same Crossbar.io router instance as the adapter connects to. Consequently, the frontend is able to invoke the procedures exposed on the Pi.

### Preparations on the Pi

[Enable audio](https://www.raspberrypi.org/documentation/configuration/audio-config.md) output on the 3.5mm plug:

```console
sudo amixer cset numid=3 1
```

The volume may be a bit low. To increase that to (near) the maximum, do

```shell
sudo amixer set PCM -- -100
```

to set this to near maximun (and try larger values instead of `-100` to decrease the volume a bit again).

Install or update `pygame`:

```shell
pip install -U pygame
```

Install Autobahn|Python

```console
sudo pip install autobahn
```

Install `treq`

```shell
pip install treq
```


### Running the Sample Player

The code for this can be found in the [crossbarexamples GitHub repository](https://github.com/crossbario/crossbarexamples) under `iotcookbook`. You need to clone this (or [download it as a ZIP file](https://github.com/crossbario/crossbarexamples/archive/master.zip)).

You need a Crossbar.io instance for the Sample Player adapter on the Pi and the browser frontend to connect to.

The simplest way is to navigate to `iotcookbook/device/pi/sampleplayer` in your local `crossbarexamples` repo, and do

```console
crossbar start
```

This will also serve the browser frontend under

```
http://localhost:8080
```

Get the player and some sample files onto the Pi, e.g. via scp

```console
scp sampleplayer_pi.py pi@<IP of your Pi>:~/
scp -r samples pi@192.168.1.136:~/
```

and then start it

```console
python sampleplayer_pi.py
```

Then use the browser frontend to trigger one of the preset samples, or upload a sample. Samples can be in WAV or OGG format. (If you have another format, then you need to convert to one of these formats.)

When uploading, the sample is stored in the `samples` folder on the Pi. It can be triggered using the provided sample name. It is automatically added to the sample set on next startup. 


## The API

The adapter exposes these procedures

* `io.crossbar.examples.iot.devices.pi.<serial_of_your_pi>.audioout.trigger_sample` - which takes the name of the sample to trigger as an argument
* `io.crossbar.examples.iot.devices.pi.<serial_of_your_pi>.audioout.stop_sample` - which takes the name of the sample whose playback should be stopped as an argument
* `io.crossbar.examples.iot.devices.pi.<serial_of_your_pi>.audioout.add_sample` - which takes the URL from which the sample is to be downloaded and the name which shall be assigned to the sample as arguments


## Using it

Store your samples on the Pi. The sample name is the filename (minus the file type ending, if any).