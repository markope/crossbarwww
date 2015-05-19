This page exlains the basic setup of the Yun.  For an overview of all materials we have concerning the Yun, see

* [Arduino Yun - Links](Arduino Yun)

<div class="topimage_container">
   <img class="topimage" src="../../static/img/iotcookbook/arduino_yun.jpg" alt="">   
</div>

We'll go over

* connecting to your wifi network
* access via SSH
* adding SSH keys for password-free login
* remote-mounting the Yun's filesystem
* updating the software

Feel free to skip any steps which you've already performed or feel aren't necessary (e.g. the adding of SSH keys or remote-mounting of the file system).

## System Recovery

Should anything go wrong with your experiments here, don't worry - the Yun includes mechanisms to:

 * **reset Wifi** network configuration to factory default
 * **restore Linux** system image to factory default

The relevant button to perform **both** of these functions is called *"Wifi Reset button"* in the Yun documentation and is located here:

![](/static/img/iotcookbook/yun/ArudinoYun_RST.jpg)

 1. Pressing the *Wifi Reset button* for >5s (but less than 30s) and then releasing will *reset the Wifi configuration to factory default*

 2. Pressing the *Wifi Reset button* for >30s and then releasing will *restore the Linux system image to factory default*

Both functions will also reboot the Yun. Restoring the system image to factory defaults also resets any wifi configuration you've done.

If you've previously tinkered around with the Yun, we suggest resetting it before following this tutorial, since it decreases chances of software/configuration conflicts.

## Network connectivity

The Yun has *two* network interfaces:

 * Ethernet (100Mb)
 * Wifi (bgn)

where each network interface has it's *own* MAC address.

For most use cases, the wifi connection will be used. 

You may want to wait with the wifi setup until after the system software update and perform the update itself using an ethernet connection. The system software update also resets the wifi settings, so you'd have to do them twice otherwise. To do so you can go directly to the ssh part of this tutorial, and then come back to the wifi configuration later.


### Ethernet

The ethernet interface on the Yun is configured by default to get an IP address via DHCP (as is the Wifi interface in client mode) from a DHCP server on your network (such as your home router).

When you plug in the ethernet, the Yun ethernet interface should get assigned an IP automatically which you can verify from the Web interface:

![](/static/img/iotcookbook/yun/network2.png)


### Wifi

When the Arduino Yun is first powered on, the Wifi will be starting in **AP-Mode** ("Access Point Mode") and the Yun creates a new wireless network on the IP range

   192.168.240.0/24

When you scan for Wifi networks, you should see a new network with a SSID as

   Arduino Yun-XXXXXXXXXXXX

where `XXXXXXXXXXXX` is the MAC address of the Yun's *Wifi* interface:

![](/static/img/iotcookbook/yun/network1.png)

This is the factory default, and when you reset the Wifi configuration, it will be the recovered again.

> Note: The ethernet interface has a *different* MAC address - see below.
> 

You can access the Web configuration interface of your Yun by connecting e.g. your notebook to the above Wifi network and then open the following URL in your browser 

```
http://192.168.240.1
```

The default administrator password is `arduino`. You might want to change that (which you can do from the Web configuration interface).

### Wifi Client Mode

When your Yun is connected via Ethernet to your network, the Yun will be able to connect to the public Internet via the default router on your network (your home router).

However, if you plan to have you Yun connecting to the Internet *without* an ethernet cable connected, you will need to reconfigure the Yun's Wifi to run in **Client Mode** and have the Yun connect to your router via Wifi as a *client*, so it can call out to the Internet.

![](/static/img/iotcookbook/yun/network3.png)

After reconfiguration, the Yun will reboot, and you now should see both network interfaces on your main LAN and with IP addresses assigned from your router:

![](/static/img/iotcookbook/yun/network4.png)

> Doing the above, the Yun will no longer function as a Wifi access point to which others Wifi clients could connect. As long as the Yuns IP is known to other peers on your network, those peers will however still be able to connect on the TCP/IP level to anything running as a server on your Yun.
> 

### Static DHCP

When your Yun gets IP addresses for its ethernet and Wifi interfaces, your router will usually select free unassigned IP addresses randomly (from its IP range) - but these IP addresses can change from time to time (or across reboots of your router).

Some home routers or advanced router OSs such as OpenWRT and DD-WRT allow to configured DHCP to assign IP addresses to certain devices statically (called "static DHCP").  That means the device will always get the same IP address.

Having you Yun get static IPs via DHCP is useful, since e.g. to login from outside into your Yun via SSH will always work with the *same* IP.

A quick look through the user interface of your router should tell you whether you can assign static IP addresses.

### SSH

Now that you have networking running for your Yun (either ethernet, Wifi or both), the next thing is to SSH into your Yun. This will allow you to do further software setup and advanced system configuration from a root shell.

The default password for `root` is `arduino`.

Here is how that looks:

```shell

$ ssh -l root 192.168.1.150
The authenticity of host '192.168.1.150 (192.168.1.150)' can't be established.
RSA key fingerprint is f9:e0:1e:bd:bb:f9:e1:33:5b:c7:5d:75:da:2c:20:b1.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '192.168.1.150' (RSA) to the list of known hosts.
root@192.168.1.150's password:


BusyBox v1.19.4 (2013-08-07 16:16:02 CEST) built-in shell (ash)
Enter 'help' for a list of built-in commands.

      ___                   ___                       ___           ___
     /\__\      ___        /\__\          ___        /\__\         /\  \
    /:/  /     /\  \      /::|  |        /\  \      /::|  |       /::\  \
   /:/  /      \:\  \    /:|:|  |        \:\  \    /:|:|  |      /:/\:\  \
  /:/  /       /::\__\  /:/|:|  |__      /::\__\  /:/|:|  |__   /:/  \:\  \
 /:/__/     __/:/\/__/ /:/ |:| /\__\  __/:/\/__/ /:/ |:| /\__\ /:/__/ \:\__\
 \:\  \    /\/:/  /    \/__|:|/:/  / /\/:/  /    \/__|:|/:/  / \:\  \ /:/  /
  \:\  \   \::/__/         |:/:/  /  \::/__/         |:/:/  /   \:\  /:/  /
   \:\  \   \:\__\         |::/  /    \:\__\         |::/  /     \:\/:/  /
    \:\__\   \/__/         /:/  /      \/__/         /:/  /       \::/  /
     \/__/                 \/__/                     \/__/         \/__/

            _______                     ________        __
           |       |.-----.-----.-----.|  |  |  |.----.|  |_
           |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
           |_______||   __|_____|__|__||________||__|  |____|
                    |__| W I R E L E S S   F R E E D O M

root@Arduino:~#

```

To change the password for `root`, type `passwd`.

For ssh, on Windows the Git shell comes with a ssh client, and on Unix-y systems, openssh is often installed by default already.


#### Public Key Authentication

Now, retyping your password each time you log in gets old fast. Public key based authentication for SSH allows you to do password-less, but nevertheless secure logins.

This isn't the place to give an introduction to SSH and public key authentication, however you should have little problems finding tutorials and information on the net. I will only cover stuff that is "unusual" on the Yun compared to a commonly seen Unix.

The Linino/OpenWRT Linux on the Yun does use Dropbear for SSH support (both client and server) - this is a different software package from usual Linux distributions and Unix systems (which is OpenSSHd).

One difference is that to enable public key based authentication for root, the authorized public keys need to be added to the following file (and not the usual `/root/.ssh/authorized_keys`):  

```text
vi /etc/dropbear/authorized_keys
chmod 0600 /etc/dropbear/authorized_keys
```

A complete tutorial for setting up public key based authentication on OpenWRT can be found [here](http://wiki.openwrt.org/oldwiki/dropbearpublickeyauthenticationhowto).


#### SSHFS

Another thing you probably want to do: mount the Yun's filesystem on your desktop via SSH.

Why is that? Mounting over SSH allows you to edit files on the Yun using your favorite editor directly *on your desktop*. So you don't need to fiddle with **vi** and such inside a shell;) E.g. I use the awesome [SublimeText](http://www.sublimetext.com/) editor on Windows. Yeah, you probably prefer something else - and that is fine, since it will work too.

This magic works via SFTP (secure FTP), which is a FTP-like protocol that runs over SSH. On the Yun side, you'll need to have the SFTP package installed, login via SSH as root and do:


```shell
opkg update
opkg install openssh-sftp-server
```

Now, on **Windows**, [Win-SSHFS](http://code.google.com/p/win-sshfs/) which you can download from [here](http://code.google.com/p/win-sshfs/downloads/detail?name=win-sshfs-0.0.1.5-setup.exe) is open-source and installs without hassles up to Windows 7 (and with a few workarounds on Windows 8 as well). It is, however, unstable. A commercial alternative (with a free version perfectly sufficient for our purposes) is [SFTP Net Drive](https://www.eldos.com/sftp-net-drive/), which works stable..

On **Mac OSX**, there is a nice tutorial [here](http://fortysomethinggeek.blogspot.de/2012/11/sshfs-on-osx-mount-sshsftp-shares-on-mac.html) that walks you through setting things up with [FUSE for OSX](http://osxfuse.github.io/).

On **Ubuntu**, you can [use Nautilus](http://www.lessons4you.info/how-to-connect-ssh-sftp-and-ftp-servers-using-nautilus-ubuntu-13-04/) or the [command line](http://howto.blbosti.com/2010/09/mount-a-remote-ssh-folder-in-ubuntu-cmd-and-gui/).

With SFTP set up, you now can simply open, edit, create, copy, delete and move files conveniently from your desktop. This can often be more comfortable than doing everything via command line SSH (and SCP).


## System update

It is a good idea to ensure that your Yun runs the most recent version of it's operating system and other software. 

Be aware that the system update also resets the wifi settings, so you'll have to go through these again!

To update we first update the yun package management:

```shell
opkg update
```

Then we need to install `unzip`:

```shell
opkg install unzip
```

We need to download the update to RAM, since there isn't enough disk space, so we switch to `tmp`, which is in RAM:

```shell
cd /tmp
```

You need to get the current link to the upgrade from the [Arduino downloads page](http://www.arduino.cc/en/Main/Software). Be aware that the link you get from this page only leads to a donation page - this then contains the actual link. We then download this

```shell
wget http://downloads.arduino.cc/openwrtyun/1/YunSysupgradeImage_v1.5.3.zip 
```

unzip it

```shell
unzip YunSysupgradeImage_v1.5.3.zip
```

and install it

```shell
sysupgrade -v -n openwrt-ar71xx-generic-yun-16M-squashfs-sysupgrade.bin
```

If you haven't set up the wifi yet, now is the time to do so. If you previously did - do it again (we told you that it would be better to use ethernet - though it's a small hassle, really).

## Next

Your Yun is now read for exanding the file system to use a microSD card - which we'll need to have the space to install Node.js + Autobahn|JS.

* [Expaning Disk Space](Arduino-Yun-Expanding-Disk-Space)

