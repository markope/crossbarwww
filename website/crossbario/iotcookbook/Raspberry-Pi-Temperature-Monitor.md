The Raspberry Pi Temperature Monitor component allows the remote monitoring of your Raspberry Pi's on-board temperature sensor. 

<div class="topimage_container">
   <img class="topimage" src="../../static/img/iotcookbook/raspberry_pi.jpg" alt="">   
</div>

## Trying it out

The code for this can be found in the [crossbarexamples GitHub repository](https://github.com/crossbario/crossbarexamples) under `iotcookbook`. You need to clone this (or [download it as a ZIP file](https://github.com/crossbario/crossbarexamples/archive/master.zip)).

Open a shell for the component directory on your computer. 

Start up Crossbar.io:

```shell
crossbar start
```

This also serves a frontend which displays the temperature and allows you to set a couple of parameters:

```
http://localhost:8080
```

In `tempmon_pi.js`, add the URL of the machine on which Crossbar.io runs:

```javascript
var connection = new autobahn.Connection({
   url: "ws://<URL OF YOUR CROSSBAR INSTANCE>/ws", // replace with the url of your crossbar instance
   realm: "iot_cookbook"
});
```

Then get `tempmon_pi.js` onto the Raspberry Pi, e.g. by doing

```console
scp tempmon_pi.js pi@<IP of your Pi>:~/
```

Now run our camera component

```shell
python tempmon_pi.py
```

This should log

```shell
2015-05-23 12:49:52+0000 [-] Log opened.
2015-05-23 12:49:52+0000 [-] Pi serial is: 6ec468fc
2015-05-23 12:49:52+0000 [-] Pi Temperature Monitor starting with ID 6ec468fc ...
2015-05-23 12:49:57+0000 [-] Running on reactor <twisted.internet.epollreactor.EPollReactor object at 0x123a570>
2015-05-23 12:49:57+0000 [-] Starting factory <autobahn.twisted.websocket.WampWebSocketClientFactory object at 0x1242e50
>
2015-05-23 12:49:57+0000 [WampWebSocketClientProtocol,client] PiMonitor connected
2015-05-23 12:49:57+0000 [WampWebSocketClientProtocol,client] Registered io.crossbar.examples.pi.6ec468fc.tempmon.get_te
mperature
2015-05-23 12:49:57+0000 [WampWebSocketClientProtocol,client] Registered io.crossbar.examples.pi.6ec468fc.tempmon.impose
_stress
2015-05-23 12:49:57+0000 [WampWebSocketClientProtocol,client] Registered io.crossbar.examples.pi.6ec468fc.tempmon.toggle
_publish
2015-05-23 12:49:57+0000 [WampWebSocketClientProtocol,client] Registered io.crossbar.examples.pi.6ec468fc.tempmon.set_th
reshold
2015-05-23 12:49:57+0000 [WampWebSocketClientProtocol,client] PiMonitor ready.
```

Once this is running, the current temperature of your Pi should be displayed in the browser.

You can toggle the publishing of the temperature, and set a threshold at which to receive a temperature alarm.

## The API

The temperature is published to the topic

```
io.crossbar.examples.pi.<your_pi_serial>.tempmon.on_temperature
``` 

Publications to this can be toggled by calling

```
io.crossbar.examples.pi.<your_pi_serial>.tempmon.toggle_publish
```

A threshold temperature can be set by calling

```
io.crossbar.examples.pi.<your_pi_serial>.tempmon.set_threshold
```

with a threshold value (integer) as the argument

For any threshold value other than '0', as long as the current temperature exceeds the threshold, the temperature is published to

```
io.crossbar.examples.pi.<your_pi_serial>.tempmon.on_threshold_exceeded
``` 

To produce a temperature increase by keeping the CPU busy, you can call

```
io.crossbar.examples.pi.<your_pi_serial>.tempmon.impose_stress
```

with an integer as an argument (values greater than 100000 are suggested).

