To get you started, we recommend the [Quick Setup](Arduino Yun Quick Setup), which is the shortest and simplest way to get your Yun talking to the world via WAMP. 

If you're interested in going thorugh the steps manually, or want more information about a particular stage of the setup process, there are the multiple specific tutorials.

The basic preparation of the Yun is covered in (you can go through these in the sequence they are listed)

* [System Recovery](Arduino Yun System Recovery): reset your Yun to have a defined state to start installing from
* [System Update](Arduino Yun System Update): update the Linux OS
* [Establishing Network Connectivity](Arduino Yun Network Connectivity): Connecting your Yun to ethernet & WiFi
* [Connecting via SSH](Arduino Yun SSH Access): connecting via SSH to administrate the Yun
* [Expanding disk space](Arduino-Yun-Expanding-Disk-Space): using a microSD card to expand the storage on the Yun
* [Disabling the serial bridge](Arduino-Yun-Disable-Bridge): disabling the default serial bridge so we can use serial for our own

To connect the Yun to WAMP applications:

* [Setting up Autobahn|Python](Arduino-Yun-AutobahnPython-Setup) if you want to use Python on the Linux part of the Yun
* [Setting up Autobahn|JS](Arduino-Yun-AutobahnJS-Setup): if you want to use JavaScript/Node.js on the Linux part of the Yun - also required for the generic serial-to-WAMP bridge
* [Generic Serial-to-WAMP Bridge](Arduino Yun Serial to WAMP Bridge): generic access to the Yun's GPIO pins from WAMP