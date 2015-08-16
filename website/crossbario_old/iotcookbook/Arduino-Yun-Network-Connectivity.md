The Yun has *two* network interfaces:

 * Ethernet (100Mb)
 * Wifi (bgn)

where each network interface has it's *own* MAC address.

For most use cases, the Wifi connection will be used.

You may want to **wait with the wifi setup if you intend to perform a system software update** and perform the update itself using an ethernet connection. The system software update also resets the wifi settings, so you'd have to do them twice otherwise. 

### Ethernet

The ethernet interface on the Yun is configured by default to get an IP address via DHCP (as is the Wifi interface in client mode) from a DHCP server on your network (such as your home router).

When you plug in the ethernet, the Yun ethernet interface should get assigned an IP automatically. 

To find out the IP you can log into the router of your network, or use a network discovery tool (e.g. [Fing](http://www.overlooksoft.com/fing), which is free, cross-platform and works well).


### Wifi

When the Arduino Yun is first powered on, the Wifi will be starting in **AP-Mode** ("Access Point Mode") and the Yun creates a new wireless network. You can configure the Yun to use your wifi by 
   * connecting to the Yun's WiFi network, 
   * calling up a configuration page it serves, and 
   * entering your wifi credentials on this. (The configuration can easily be done on a smartphone or tablet if your dev machine does not have wifi.)

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
