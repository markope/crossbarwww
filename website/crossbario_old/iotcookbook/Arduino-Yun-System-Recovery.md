Should anything go wrong with your experiment with the Yun, then don't worry - the Yun includes mechanisms to:

 * **reset the Wifi network configuration** to factory default
 * **restore the Linux system image** to factory default

The relevant button to perform **both** of these functions is called *"Wifi Reset button"* in the Yun documentation and is located here:

![](/static/img/iotcookbook/yun/ArudinoYun_RST.jpg)

Make sure the Yun is fully booted before performing reset/recovery. Then:

 1. Pressing the *Wifi Reset button* for >5s (but less than 30s) and then releasing will *reset the Wifi configuration to factory default*

 2. Pressing the *Wifi Reset button* for >30s and then releasing will *restore the Linux system image to factory default*. This means the last image you flashed if you've updated the system.

Both functions will also reboot the Yun (after releasing the button). Restoring the system image to factory defaults also resets any Wifi configuration you've done.

If you've previously tinkered around with the Yun, we suggest resetting it before following any of our tutorials, since it decreases chances of software/configuration conflicts.