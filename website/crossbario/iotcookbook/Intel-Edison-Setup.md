## Firmware Update

In general, the Edison is a very handsome device. However, firmware update, as with other devices, can be tricky.

There are recipes on the Web for updating the firmware using different methods and on different host systems. The entry point on the Intel docs is [here](https://software.intel.com/en-us/flashing-your-firmware-edison).

The method that worked for me is on Windows and using the [Flash Tool Lite](https://software.intel.com/de-de/using-flash-tool-lite). Install this tool.

Then, goto [Intel Edison downloads](https://software.intel.com/en-us/iot/hardware/edison/downloads) and download the [latest firmware](http://downloadmirror.intel.com/25028/eng/edison-image-ww25.5-15.zip). No need to unzip the image.

Make sure the little switch on the Edison expansion board points towards the two micro USB connectors. But do NOT yet connect the Edison to your computer! The order (and timing) of the following steps is essential.

1. Start Intel Flash Tool Lite
2. Connect the micro USB J3 on the Edison expansion board to your computer (but NOT the other USB!)
3. Select downloaded image (click the "Browse" button)
4. Select "Configuration: RNDIS" (Windows) or "Configuration: CDC" (Linux)
5. Click "Start to flash"
6. Now (yes, only now!), quickly (!) first plug in the 2nd micro USB (J16)
connecting to your computer, and secondly plug in external power supply

The tool should now detect the device and start to flash. If everything
works fine, this will finish in 3-5 minutes.

If it doesn't work, try to repeat. As said, this can be tricky.


## Wifi and SSH configuration

To configure the Wifi, you will need to login to your Edison via serial initially. After Wifi has been configured, you can remotely login to the Edison via SSH.

Connect the J3 micro-USB on the Edison expansion board to your computer.

On Windows, follow [this](https://software.intel.com/en-us/setting-up-serial-terminal-on-system-with-windows) for using Putty to login via serial.

On Linux, do:

```console
sudo apt-get install screen
sudo screen /dev/ttyUSB0 115200
```

Then hit RETURN twice and login as `root`. You don't need as password when logging in via serial. Then, configure the Edison's name, Wifi and root password (required for SSH) by doing:

```console
configure_edison --name
configure_edison --wifi
configure_edison --password
reboot
```

When the Edison has rebooted, you should be able to log into the Edison via SSH from your local network the Edison has connected to.

After the update, you can check what version is running:

```console
root@Edison2:~# uname -a
Linux Edison2 3.10.17-poky-edison+ #1 SMP PREEMPT Fri Jun 19 12:06:40 CEST 2015 i686 GNU/Linux
root@Edison2:~# configure_edison --version
159
```

## Install MRAA

Intel has published [MRAA](https://github.com/intel-iot-devkit/mraa), an open-source library for hardware access from high-level languages running on the Linux CPU such as C/C++, Python, JavaScript.

We'll be using this library. To install, login to the Edison and:

```console
opkg update
opkg install libmraa0
```

You can find the docs here:

* [MRAA Python documention](http://iotdk.intel.com/docs/master/mraa/python)
* [MRAA JavaScript documentation](http://iotdk.intel.com/docs/master/mraa/node/modules/mraa.html)


## Install AutobahnPython

To install AutobahnPython, first configure additional pacakge repositories on the Edison. Login to the Edison and edit `/etc/opkg/base-feeds.conf` for:

```
src/gz all http://repo.opkg.net/edison/repo/all
src/gz edison http://repo.opkg.net/edison/repo/edison
src/gz core2-32 http://repo.opkg.net/edison/repo/core2-32
```

Then do

```console
opkg update
opkg install python-pip
pip install autobahn[twisted,accelerate,serialization]
```

This will take some minutes. You can check the installation:

```console
root@Edison2:~# python
Python 2.7.3 (default, Jun 19 2015, 07:08:38)
[GCC 4.9.1] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import autobahn
>>> autobahn.__version__
'0.10.5'
>>>
```

You can also use the following simple [blinking program](https://github.com/crossbario/crossbarexamples/blob/master/iotcookbook/device/edison/blinky/blinky.py) to test:

```python
import mraa
import time

x = mraa.Gpio(13)
x.dir(mraa.DIR_OUT)

while True:
    x.write(1)
    time.sleep(0.2)
    x.write(0)
    time.sleep(0.2)
```


## Install AutobahnJS

To install AutobahnPython, first configure additional pacakge repositories on the Edison. Login to the Edison and edit `/etc/opkg/base-feeds.conf` for:

```
src/gz all http://repo.opkg.net/edison/repo/all
src/gz edison http://repo.opkg.net/edison/repo/edison
src/gz core2-32 http://repo.opkg.net/edison/repo/core2-32
```

Then do

```console
opkg update
opkg install nodejs
npm install -g autobahn
```

This will take some minutes. You can check the installation:

```console
root@Edison2:~# node --version
v0.10.40
root@Edison2:~# node
> var autobahn = require('autobahn');
undefined
> autobahn.version
'0.9.6'
>
```

You can also use the following simple [blinking program](https://github.com/crossbario/crossbarexamples/blob/master/iotcookbook/device/edison/blinky/blinky.js) to test:

```python
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
```

## Tutorials

<img src="../../static/img/iotcookbook/edison/edison_with_tinkerkit.jpg" alt="">

* https://github.com/crossbario/crossbarexamples/tree/master/iotcookbook/device/edison/tutorial/tutorial1
* https://github.com/crossbario/crossbarexamples/tree/master/iotcookbook/device/edison/tutorial/tutorial2
