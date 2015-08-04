This recipe describes how to install Autobahn|Python on the Yun.

> Please make sure you have expanded the Yun's disk space, as the onboard Flash hasn't enough space left.

## Dependencies

First, install dependencies. Login to the Yun and

```console
opkg update
opkg install bzip2
opkg install unzip
opkg install tar
opkg install wget
opkg install distribute
opkg install bzip2
opkg install pyopenssl
opkg install python-openssl
opkg install python-crypto
opkg install python-bzip2
opkg install python-ncurses
```

Then install [pip](https://pip.pypa.io/), a modern package manager for Python

```console
easy_install pip
```

> With this, and the subsequent steps: please be patient, the Yun hasn't a lot of steam, and since we are using a SD card overlay, things are slow installing.


## Twisted

[Autobahn|Python](http://autobahn.ws/python/) supports two underlying network libraries: [Twisted](http://twistedmatrix.com/) and [asyncio](https://docs.python.org/3.4/library/asyncio.html). We'll be using Twisted:

```console
pip install zope.interface
```

Download the Twisted source archive

```console
cd /root
wget --no-check-certificate https://pypi.python.org/packages/source/T/Twisted/Twisted-15.3.0.tar.bz2
tar xvjf Twisted-15.3.0.tar.bz2
cd Twisted-15.3.0
```

Now edit `setup.py` and comment out line 63 (see [here](http://stackoverflow.com/a/5128593/884770), [here](https://twistedmatrix.com/trac/ticket/6853), [here](https://twistedmatrix.com/trac/ticket/3586) and [here](https://twistedmatrix.com/trac/ticket/6831)):

    #        conditionalExtensions=getExtensions(),

> Note: The number of the line to be commented (L63) might change with future Twisted versions. The relevant thing is to comment the `conditionalExtensions=..` statement.
>  

Then build and install Twisted:

```console
python setup.py install
```

This will take a long time. Be patient;) The Yun doesn't have a lot of steam and we are installing onto a micro SD card, which means low filesystem performance on top.


## pySerial

Since we want to talk to the MCU from the main CPU via serial, install Python serial support via [pySerial](https://pypi.python.org/pypi/pyserial):

```console
pip install pyserial
```

## AutobahnPython

Finally, for WebSocket/WAMP protocol support install [Autobahn|Python](https://pypi.python.org/pypi/autobahn/):

```console
pip install autobahn
```
