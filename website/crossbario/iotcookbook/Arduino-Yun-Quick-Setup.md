## Get the image

Download the [image](https://s3-eu-west-1.amazonaws.com/crossbar.io/download/autobahn_yun_extroot.zip) and write the image to an SD card.

The SD card MUST have a size of at least 1GB. Also, a fast SD card (Class 10) is recommended.

On Windows, you can use [Win32 Disk Imager](http://sourceforge.net/projects/win32diskimager/).

On Linux, the following will do (**change the SD card device in below!**):

```console
cd /tmp
wget https://s3-eu-west-1.amazonaws.com/crossbar.io/download/autobahn_yun_extroot.zip
unzip autobahn_yun_extroot.zip
sudo dd if=/tmp/autobahn_yun_extroot.img of=/dev/sde bs=1M
```

## Update the Yun

Login to your Yun and run [this script](https://raw.githubusercontent.com/crossbario/crossbarexamples/master/iotcookbook/device/yun/quickinstall/step1.sh) to update the Yun

```console
cd /tmp
curl http://bit.ly/1IXKbTU -Lko step1.sh
sh step1.sh
```

The Yun will now reboot.

> Note: part of the image update involves recreating SSH host keys on the Yun. When you login next time, you might get a SSH warning/error mentioning a "potential security breach". That's ok, just delete the old SSH host key (the error message gives a hint how to do that).


## Activate the SD card

Insert the SD card and run [this script](https://raw.githubusercontent.com/crossbario/crossbarexamples/master/iotcookbook/device/yun/quickinstall/step2.sh) on the Yun to activate the SD card

```console
cd /tmp
curl http://bit.ly/1P6OxHb -Lko step2.sh
sh step2.sh
```

The Yun will now reboot. Done!

**You now have AutobahnPython (on Python/Twstied) and AutobahnJS (on NodeJS) setup on the Yun.**

