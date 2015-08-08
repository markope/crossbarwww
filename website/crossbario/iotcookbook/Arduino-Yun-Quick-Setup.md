This quick setup represents the simplest, fastest way we could find to get the software necessary to connect to a WAMP router onto the Yun. Once you've completed this you'll be able to run WAMP components in Python or JavaScript/Node.js, as well as use the generic serial-to-WAMP bridge.

We recommend the quick setup if you just want to start using the Yun as part of a WAMP application. In case you want to learn more about the Yun, or need to modify parts things, the specific tutorials give you information about individual aspects of setting up the Yun. 

## Get the image

Download the [image](https://s3-eu-west-1.amazonaws.com/crossbar.io/download/autobahn_yun_extroot.zip) and write the image to an SD card.

The SD card MUST have a size of at least 1GB. Also, a fast SD card (Class 10) is highly recommended, since otherwise things may take a while.

On Windows, you can use [Win32 Disk Imager](http://sourceforge.net/projects/win32diskimager/) for writing the image.

On Linux, the following will do (**change the SD card device in below!**):

```console
cd /tmp
wget https://s3-eu-west-1.amazonaws.com/crossbar.io/download/autobahn_yun_extroot.zip
unzip autobahn_yun_extroot.zip
sudo dd if=/tmp/autobahn_yun_extroot.img of=/dev/sde bs=1M
```

## Update the Yun

Login to your Yun and do

```console
cd /tmp
curl http://bit.ly/1IXKbTU -Lko step1.sh
sh step1.sh
```

which will download and run [this script](https://raw.githubusercontent.com/crossbario/crossbarexamples/master/iotcookbook/device/yun/quickinstall/step1.sh).

The Yun will now reboot.

> Note: part of the image update involves recreating SSH host keys on the Yun. When you login next time, you might get a SSH warning/error mentioning a "potential security breach". That's ok, just delete the old SSH host key (the error message gives a hint how to do that).


## Activate the SD card

Insert the SD card and do

```console
cd /tmp
curl http://bit.ly/1P6OxHb -Lko step2.sh
sh step2.sh
```

which downloads and runs [this script](https://raw.githubusercontent.com/crossbario/crossbarexamples/master/iotcookbook/device/yun/quickinstall/step2.sh) on the Yun to activate the SD card

The Yun will now reboot. Done!

**You now have AutobahnPython (on Python/Twstied) and AutobahnJS (on NodeJS) setup on the Yun, as well as a generic serial-to-WAMP bridge.**

## Next

Check out the components and apps for the Arduino Yun (listed on the [Arduino Yun entry page](Arduino-Yun)) - there's a change you'll find the functionality you require already implemented.

Read about how to use the [serial-to-WAMP bridge](Arduin Yun Serial to WAMP Bridge).

Learn step-by-step about the basics of programming the Yun with our three-part tutorial for 

* [Python](Arduino Yun Python Tutorial)
* [JavaScript/Node.js](Arduino Yun JavaScript Tutorial)



