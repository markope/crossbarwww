[Ubuntu Snappy](http://www.ubuntu.com/cloud/tools/snappy) is a new kind of server operating system that uses a transactional updating scheme for applications.
Crossbar.io publishes an official binary distribution for Ubuntu Snappy.

> Note: Ubuntu Snappy is a specialised version of regular Ubuntu. If you are using regular Ubuntu, please read [Installing on Ubuntu](Installing on Ubuntu) for installation instructions.

## Installing

On your Ubuntu Snappy server, run:

```console
sudo snappy install crossbar.crossbar
```

> The crossbar.crossbar name is because it is the Crossbar package published by Crossbar.

This will download and install Crossbar.

You can check the version installed by running:

```console
(amd64)ubuntu@ubuntu-core-stable-2:~$ sudo snappy list
Name          Date       Version Developer
ubuntu-core   2015-04-23 2       ubuntu
crossbar      2015-05-06 0.10.4  crossbar
generic-amd64 2015-04-23 1.1
```

To verify the installation:

```console
(amd64)ubuntu@ubuntu-core-stable-2:~$ crossbar.crossbar version

Crossbar.io package versions and platform information:

Crossbar.io                  : 0.10.4

  Autobahn|Python            : 0.10.3
    WebSocket UTF8 Validator : ?
    WebSocket XOR Masker     : ?
    WAMP JSON Codec          : stdlib
    WAMP MsgPack Codec       : msgpack-python-0.4.6
  Twisted                    : 15.1.0-EPollReactor
  Python                     : 2.7.8-PyPy

OS                           : Linux-3.19.0-15-generic-x86_64-with-glibc2.2.5
Machine                      : x86_64
```
