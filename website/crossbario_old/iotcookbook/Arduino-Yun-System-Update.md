It is a good idea to ensure that your Yun runs the most recent version of its operating system and other software.

Be aware that the system update also resets the Wifi settings, so you'll have to go through these again if you've set up the Yun to connect to your WiFi!

There are two ways to update the Yun's System:

* via the Web interface
* via SSH

## Updating via the Web interface

If the Yun serves as a WiFi access point (i.e. you haven't yet configured it to connect to a WiFi network) the Web interface is served at ```http://192.168.240.1```. If you've connected via WiFi, or are connected via Ethernet, you get to it via the IP that the Yun has been assigned in your network (check in your router, or use a tool like Fing, which is available for multiple systems including mobiles).

You need to get the download  to the upgrade from the [Arduino downloads page](http://www.arduino.cc/en/Main/Software) and store it locally.

Then log into the Web interface (the default password is 'arduino') and select the **advanced configuration panel** at the top of the page. Then select the **System tab**, and on this **Backup / Flash Firmware**. You can then upload the firmware image from your computer to the Yun and flash this.

## Updating via SSH

There's a description for how to do [SSH access to the Yun](Arduino Yun SSH Access).

You can use the script we provide, and just do

```console
cd /tmp
curl http://bit.ly/1IXKbTU -Lko step1.sh
sh step1.sh
```

or do things yourself if you want to get into the gritty details of what's happening:

First update the yun package management:

```console
opkg update
```

Then we need to install `unzip`:

```console
opkg install unzip
```

We need to download the update to RAM, since there isn't enough disk space, so we switch to `tmp`, which is in RAM:

```console
cd /tmp
```

You need to get the current link to the upgrade from the [Arduino downloads page](http://www.arduino.cc/en/Main/Software). Scroll down a bit untill you get to 'Other Software' and click on the 'OpenWRT - Yun 1.x.x Upgrade Image'. Be aware that the link you get from this page only leads to a donation page - this then contains the actual link. We then download this, e.g. 

```console
wget http://downloads.arduino.cc/openwrtyun/1/YunSysupgradeImage_v1.5.3.zip
```

unzip it

```console
unzip YunSysupgradeImage_v1.5.3.zip
```

and install it

```console
sysupgrade -v -n openwrt-ar71xx-generic-yun-16M-squashfs-sysupgrade.bin
```

Please be patient. This takes a couple of minutes, and will finally reboot the Yun when done:

```console
root@Arduino:/tmp# sysupgrade -v -n openwrt-ar71xx-generic-yun-16M-squashfs-sysupgrade.bin
Sending TERM to remaining processes ... uhttpd dbus-daemon dnsmasq avahi-daemon thd ntpd uSDaemon sleep syslogd klogd hotplug2 ubusd netifd
Sending KILL to remaining processes ... uhttpd
Switching to ramdisk...
Performing system upgrade...
Unlocking firmware ...

Writing from <stdin> to firmware ...  [w]

Upgrade completed
Rebooting system...
```

> Note: On the next connect via SSH, you'll get a security warning, since the upgrade and the reset it did led to the creation of new SSH keys. You need to delete the previous SSH key from your keys file. This should be in the `.ssh` directory in your user directory. Each key here is one line, and the warning gives you the number of the line you need to delete. After you've deleted this, you'll be asked to accept the new SSH key since this is now considered an initial connect again.

After updating, here is what I get:

```console
root@Arduino:~# uname -a
Linux Arduino 3.3.8 #1 Fri Nov 14 08:57:34 CET 2014 mips GNU/Linux
root@Arduino:~# dmesg | awk 'NR==1'
[    0.000000] Linux version 3.3.8 (jenkins@jenkins) (gcc version 4.6.3 20120201 (prerelease) (Linaro GCC 4.6-2012.02) ) #1 Fri Nov 14 08:57:34 CET 2014
```

## Next

If you haven't [set up the Wifi](Arduin Yun Network Connectivity) yet, now is the time to do so. If you previously did - do it again (we told you that it would be better to use ethernet - though it's a small hassle, really).