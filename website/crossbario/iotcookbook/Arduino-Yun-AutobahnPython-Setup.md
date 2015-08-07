This recipe describes how to install Autobahn|Python on the Yun.

> Please make sure you have expanded the Yun's disk space, as the onboard Flash hasn't enough space.

## Dependencies

First, install required dependencies. Login to the Yun and

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

Then install [pip](https://pip.pypa.io/), a modern package manager for Python:

```console
easy_install pip
```

> With this, and the subsequent steps: please be patient, the Yun hasn't a lot of steam, and since we are using a SD card overlay, things are slow installing.


## pySerial

Since we want to talk to the MCU from the main CPU via serial, install Python serial support via [pySerial](https://pypi.python.org/pypi/pyserial):

```console
pip install pyserial
```


## Twisted

[Autobahn|Python](http://autobahn.ws/python/) supports two underlying network libraries: [Twisted](http://twistedmatrix.com/) and [asyncio](https://docs.python.org/3.4/library/asyncio.html).

**Here we explain how to setup Twisted. You only need one of both: either Twisted or asyncio (not both)**.

First, install this dependency:

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


## asyncio

[Autobahn|Python](http://autobahn.ws/python/) supports two underlying network libraries: [Twisted](http://twistedmatrix.com/) and [asyncio](https://docs.python.org/3.4/library/asyncio.html).

**Here we explain how to setup asyncio. You only need one of both: either Twisted or asyncio (not both)**.

Installing asyncio (more precisely, Trollius, a backport of asyncio to Python 2) is easy:

```console
pip install trollius
```


## AutobahnPython

Finally, for WebSocket/WAMP protocol support install [Autobahn|Python](https://pypi.python.org/pypi/autobahn/):

```console
pip install autobahn
```

To test your setup:

```console
root@Arduino:~# python
Python 2.7.3 (default, Nov 13 2014, 21:40:08) 
[GCC 4.6.3 20120201 (prerelease)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import autobahn
>>> autobahn.__version__
'0.10.5'
>>> 
```

Congrats!
