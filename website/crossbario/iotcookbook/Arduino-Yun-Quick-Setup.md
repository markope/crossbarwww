Write me.

## burn card

First, download the image

```console
cd /tmp
wget https://s3-eu-west-1.amazonaws.com/crossbar.io/download/autobahn_yun_extroot.zip
unzip autobahn_yun_extroot.zip
```

```console
sudo fdisk -l
umount /dev/sdf1
```

```console
sudo dd if=/tmp/autobahn_yun_extroot.img of=/dev/sdf bs=1M
```

## update sys

```console
cd /tmp
wget --no-check-certificate http://bit.ly/1IXKbTU -O step1.sh
sh step1.sh
```

https://raw.githubusercontent.com/crossbario/crossbarexamples/master/iotcookbook/device/yun/quickinstall/step1.sh

http://bit.ly/1IXKbTU


## activate card

insert card

```console
cd /tmp
wget --no-check-certificate http://bit.ly/1P6OxHb -O step2.sh
sh step2.sh
``` 

https://raw.githubusercontent.com/crossbario/crossbarexamples/master/iotcookbook/device/yun/quickinstall/step2.sh

http://bit.ly/1P6OxHb

## fix

cp /.extroot.md5sum /tmp/overlay-disabled/etc/extroot.md5sum



=======================


sudo apt-get update
sudo apt-get install git-core build-essential libssl-dev libncurses5-dev unzip

cd ~/scm/3rdparty
git clone git://git.openwrt.org/openwrt.git



http://fibasile.github.io/arduino-yun-custom-buildroot.html

Install dependencies:

```console
sudo apt-get update
sudo apt-get install subversion build-essential git-core libncurses5-dev zlib1g-dev gawk asciidoc \
bash bc binutils bzip2 fastjar flex g++ gcc util-linux zlib1g-dev libncurses5-dev \
libssl-dev perl-modules python2.7-dev rsync ruby sdcc unzip wget gettext xsltproc \
zlib1g-dev libxml-parser-perl
```

Clone the Linino repo:

```console
git clone https://github.com/arduino/linino.git
```

```console
cd linino/trunk
vim feeds.conf.default
```

```
src-git packages https://github.com/openwrt/packages.git
src-git luci http://git.openwrt.org/project/luci.git
src-svn xwrt http://x-wrt.googlecode.com/svn/trunk/package
```

> See [OpenWRT feeds](http://wiki.openwrt.org/doc/devel/feeds)


```console
cd linino/trunk
./scripts/feeds update -a
./scripts/feeds install -a
yes "" | make oldconfig
```


Install the Arduino IDE
Upload Firmata standard firmware to the Arduino microcontroller


Update system
Expand disk space
Disable serial bridge
Install NodeJS
Install Firmata-WAMP bridge




sudo umount /dev/sdf


sudo dd if=/dev/sdf of=/tmp/autobahn_yun_extroot.img bs=1M count=900
zip -j -9 /tmp/autobahn_yun_extroot.zip /tmp/autobahn_yun_extroot.img


oberstet@corei7ub1310:~/test8$ ls -la /tmp/autobahn_yun_extroot.*
-rw-r--r-- 1 root     root     943718400 Aug  5 19:42 /tmp/autobahn_yun_extroot.img
-rw-rw-r-- 1 oberstet oberstet  49212531 Aug  5 19:46 /tmp/autobahn_yun_extroot.zip


time sudo dd if=/tmp/autobahn_yun_extroot.img of=/dev/sdf bs=1M



=======================0

oberstet@corei7ub1310:~$ ./arduino-1.6.5/arduino 
Picked up JAVA_TOOL_OPTIONS: 

Der Sketch verwendet 1.124 Bytes (3%) des Programmspeicherplatzes. Das Maximum sind 32.256 Bytes.
Globale Variablen verwenden 9 Bytes (0%) des dynamischen Speichers, 2.039 Bytes für lokale Variablen verbleiben. Das Maximum sind 2.048 Bytes.
avrdude: ser_open(): can't open device "COM1": No such file or directory
ioctl("TIOCMGET"): Inappropriate ioctl for device
Build-Optionen wurden verändert, alles wird neu gebaut

Der Sketch verwendet 4.842 Bytes (16%) des Programmspeicherplatzes. Das Maximum sind 28.672 Bytes.
Globale Variablen verwenden 151 Bytes (5%) des dynamischen Speichers, 2.409 Bytes für lokale Variablen verbleiben. Das Maximum sind 2.560 Bytes.
processing.app.debug.RunnerException
    at cc.arduino.packages.uploaders.SerialUploader.uploadUsingPreferences(SerialUploader.java:131)
    at processing.app.debug.Compiler.upload(Compiler.java:165)
    at processing.app.Sketch.upload(Sketch.java:1167)
    at processing.app.Sketch.exportApplet(Sketch.java:1141)
    at processing.app.Sketch.exportApplet(Sketch.java:1113)
    at processing.app.Editor$DefaultExportHandler.run(Editor.java:2380)
    at java.lang.Thread.run(Thread.java:745)
Caused by: processing.app.SerialException: Fehler beim Ansprechen des seriellen Ports "/dev/ttyACM0".
    at processing.app.Serial.touchForCDCReset(Serial.java:92)
    at cc.arduino.packages.uploaders.SerialUploader.uploadUsingPreferences(SerialUploader.java:120)
    ... 6 more
Caused by: jssc.SerialPortException: Port name - /dev/ttyACM0; Method name - openPort(); Exception type - Permission denied.
    at jssc.SerialPort.openPort(SerialPort.java:170)
    at processing.app.Serial.touchForCDCReset(Serial.java:86)
    ... 7 more
oberstet@corei7ub1310:~$ sudo usermod -a -G dialout oberstet
[sudo] password for oberstet: 
