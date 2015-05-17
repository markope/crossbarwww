The Raspberry Pi Camera component allows the remote triggering of a photo via a WAMP procedure call. The photo is returned as the call result. 

## Trying it out

The Pi should support most standard WebCams once you've done

```shell
sudo apt-get install fswebcam
```

To try it whether this works, do

```shell
fswebcam image.jpg
```

and then open the image.

Then open a shell for the component directory on your computer. 

Start up Crossbar.io:

```shell
crossbar start
```

This also serves a frontend which allows you to trigger the taking of an image and displays the progress feedback as well as the image:

```
http://localhost:8080
```

In `camera_pi.js`, add the URL of the machine on which Crossbar.io runs:

```javascript
var connection = new autobahn.Connection({
   url: "ws://<URL OF YOUR CROSSBAR INSTANCE>/ws", // replace with the url of your crossbar instance
   realm: "iot_cookbook"
});
```

Then get `camera_pi.js` onto the Raspberry Pi, e.g. by doing

```console
scp camera_pi.js pi@<IP of your Pi>:~/
```

`camera_pi.js` is run using Node.js, so you need this installed, and additionally Autobahn|JS. Once you've got Node.js, in the directory where `camera_pi.js`is, do

```shell
npm install autobahn
```

Run it using Node.js

```shell
nodejs camera_pi.js
```

This should log

```shell
Raspberry Pi Camera starting
connected
Procedure 'io.crossbar.examples.pi.camera.take_photo' registered: 1902454329
```

Once this is running, in the browser frontend click on `take photo`. The standard burglar should be replaced with an image of whatever is in front of your webcam.

## The API

The component exposes a single procedure

```
io.crossbar.examples.pi.camera.take_photo
```

The result is a base64 encoded image. As a default this is JPG, but can be changed (in 'camera_pi.js', see the [fswebcam documentation](http://manpages.ubuntu.com/manpages/lucid/man1/fswebcam.1.html)). Due to the encoding using 'uuencode' on the Pi, header & footer need to be removed before this can be used in a data URI.

## Using it

In your own project:


* Adapt the procedure URL for taking a photo to your own needs. 

