

Goto https://software.intel.com/en-us/iot/hardware/edison/downloads and download latest image

```console
cd /media/oberstet/Edison
rm -rf *
rfm -rf \.*
wget http://downloadmirror.intel.com/25028/eng/edison-image-ww25.5-15.zip
unzip edison-image-ww25.5-15.zip
```


```console
sudo apt-get install screen
sudo screen /dev/ttyUSB0 115200
```

Then hit RETURN twice and login as `root`.


configure_edison --name
configure_edison --wifi
configure_edison --password
shutdown -h -P


root@edison:~# uname -a
Linux edison 3.10.17-poky-edison+ #1 SMP PREEMPT Wed Aug 20 16:09:18 CEST 2014 i686 GNU/Linux



sudo apt-get install gdebi libncurses5:i386 libstdc++6:i386 
wget http://downloadmirror.intel.com/24910/eng/phoneflashtoollite_5.2.4.0_linux_x86_64.deb
sudo gdebi phoneflashtoollite_5.2.4.0_linux_x86_64.deb


/usr/bin/phoneflashtoollite


* Edison1
* FC:C2:DE:30:EE:59
* edison1.office.tavendo.de
* 192.168.1.149
* root pw: edison123


* Edison2
* FC:C2:DE:36:B0:5B
* edison1.office.tavendo.de
* 192.168.1.143
* root pw: edison123


====

opkg update
opkg install libmraa0

https://github.com/intel-iot-devkit/mraa
http://iotdk.intel.com/docs/master/mraa/python
http://iotdk.intel.com/docs/master/mraa/node/modules/mraa.html


/etc/opkg/base-feeds.conf

src/gz all http://repo.opkg.net/edison/repo/all
src/gz edison http://repo.opkg.net/edison/repo/edison
src/gz core2-32 http://repo.opkg.net/edison/repo/core2-32

opkg update

===

opkg update
opkg install python-pip
pip install autobahn[twisted,accelerate,serialization]


root@Edison2:~# python
Python 2.7.3 (default, Jun 19 2015, 07:08:38) 
[GCC 4.9.1] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import autobahn
>>> autobahn.__version__
'0.10.5'
>>> 



http://iotdk.intel.com/docs/master/mraa/python/





import mraa
import time

x = mraa.Gpio(13)
x.dir(mraa.DIR_OUT)

while True:
    x.write(1)
    time.sleep(0.2)
    x.write(0)
    time.sleep(0.2)



==============

opkg update
opkg install nodejs

npm install -g autobahn


root@Edison2:~# node --version
v0.10.40
root@Edison2:~# node
> var autobahn = require('autobahn');
undefined
> autobahn.version
'0.9.6'
> 



https://communities.intel.com/thread/58813



var mraa = require('mraa');
var led = new mraa.Gpio(13);
led.dir(mraa.DIR_OUT);
var led_state = true;

function toggle_led () {
  led.write(led_state ? 1 : 0);
  led_state = !led_state;
  setTimeout(toggle_led, 200);
}

toggle_led();

