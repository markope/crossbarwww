In this recipe we will use **Crossbar**.io to generate an application template for a [WAMP](http://wamp.ws/) application written in JavaScript using [AutobahnCpp](https://github.com/tavendo/AutobahnCpp), an open-source C++ 11 WAMP implementation. The generated application includes a JavaScript frontend to run in a browser.

The frontend and backend components will talk with each other using all four main interactions available in WAMP:

 1. call a remote procedure
 2. register a procedure for remote calling
 3. publish an event to a topic
 4. subscribe to a topic to receive events

We will run the whole application with **Crossbar**.io serving as a WAMP router, static Web server and C++/Autobahn application component host.

# Prerequisites

This example requires a (decent) C++ 11 compiler, Boost, MsgPack and AutobahnCpp. For installation, please see [here](https://github.com/tavendo/AutobahnCpp#building).

# Create an example application

To create a new **Crossbar**.io node and generate a [C++ 11](http://www.php.net/) / [AutobahnCpp](https://github.com/voryx/Thruway)-based "Hello world!" example application:

```console
crossbar init --template hello:cpp --appdir $HOME/hello
```

This will initialize a new node and application under `$HOME/hello` using the application template `hello:cpp`.

> To get a list of available templates, use `crossbar templates`.

You should see the application template being initialized:

```console
oberstet@ubuntu1404:~$ crossbar init --template hello:cpp --appdir $HOME/hello
Crossbar.io application directory '/home/oberstet/hello' created
Initializing application template 'hello:cpp' in directory '/home/oberstet/hello'
Creating directory /home/oberstet/hello/autobahn
Creating directory /home/oberstet/hello/.crossbar
Creating directory /home/oberstet/hello/web
Creating file      /home/oberstet/hello/SConstruct
Creating file      /home/oberstet/hello/hello.cpp
Creating file      /home/oberstet/hello/README.md
Creating file      /home/oberstet/hello/autobahn/autobahn.hpp
Creating file      /home/oberstet/hello/autobahn/autobahn_impl.hpp
Creating file      /home/oberstet/hello/.crossbar/config.json
Creating file      /home/oberstet/hello/web/index.html
Creating file      /home/oberstet/hello/web/autobahn.min.js
Application template initialized

Now build the example by doing 'scons', start Crossbar using 'crossbar start' and open http://localhost:8080 in your browser.
```

# Build the example

To build the example:

```console
cd $HOME/hello
scons
```

# Start the node

Start your new **Crossbar**.io node using:

```console
cd $HOME/hello
crossbar start
```

You should see the node starting:

```console
oberstet@ubuntu1404:~/hello$ crossbar start
oberstet@ubuntu1404:~/hello$ crossbar start
2014-06-25 17:38:01+0200 [Controller  15889] Log opened.
2014-06-25 17:38:01+0200 [Controller  15889] ============================== Crossbar.io ==============================

2014-06-25 17:38:01+0200 [Controller  15889] Crossbar.io 0.9.6 starting
2014-06-25 17:38:01+0200 [Controller  15889] Running on CPython using EPollReactor reactor
2014-06-25 17:38:01+0200 [Controller  15889] Starting from node directory /home/oberstet/hello/.crossbar
2014-06-25 17:38:01+0200 [Controller  15889] Starting from local configuration '/home/oberstet/hello/.crossbar/config.json'
2014-06-25 17:38:01+0200 [Controller  15889] No WAMPlets detected in enviroment.
2014-06-25 17:38:01+0200 [Controller  15889] Starting Router with ID 'worker1' ..
2014-06-25 17:38:02+0200 [Router      15898] Log opened.
2014-06-25 17:38:02+0200 [Router      15898] Running under CPython using EPollReactor reactor
2014-06-25 17:38:02+0200 [Router      15898] Entering event loop ..
2014-06-25 17:38:02+0200 [Controller  15889] Router with ID 'worker1' and PID 15898 started
2014-06-25 17:38:02+0200 [Router      15898] Monkey-patched MIME table (0 of 551 entries)
2014-06-25 17:38:02+0200 [Router      15898] Site starting on 8080
2014-06-25 17:38:02+0200 [Controller  15889] Router 'worker1': transport 'transport1' started
2014-06-25 17:38:02+0200 [Router      15898] CrossbarWampRawSocketServerFactory starting on 8090
2014-06-25 17:38:02+0200 [Controller  15889] Router 'worker1': transport 'transport2' started
2014-06-25 17:38:02+0200 [Controller  15889] Starting Guest with ID 'worker2' ..
2014-06-25 17:38:02+0200 [Controller  15889] GuestWorkerClientProtocol.connectionMade
2014-06-25 17:38:02+0200 [Controller  15889] Guest with ID 'worker2' and PID 15901 started
2014-06-25 17:38:02+0200 [Controller  15889] Guest 'worker2': started
2014-06-25 17:38:02+0200 [Guest       15901] Running on 105600
2014-06-25 17:38:02+0200 [Guest       15901] Starting ASIO I/O loop ..
2014-06-25 17:38:02+0200 [Guest       15901] Connected to server
2014-06-25 17:38:02+0200 [Guest       15901] Session joined to realm with session ID 343376116645604
2014-06-25 17:38:02+0200 [Guest       15901] Registered with registration ID 1681259211686656
...
```

The Crossbar example configuration has started a WAMP router and a guest worker running the PHP/Thruway based application component. It also runs a Web server for serving static Web content.


# Open the frontend

Open [`http://localhost:8080/`](http://localhost:8080/) (or wherever Crossbar runs) in your browser. When you watch the browser's JavaScript console, you should see

> ![](/static/img/docs/shots/hello_cpp.png)

Hooray! That means: it works;)

You have just called a C++ procedure from JavaScript running in the browser. The call was transferred via WAMP, and routed by **Crossbar**.io between the application front- and backend components.

# Hacking the code

All the C++ backend code is in the file `hello.cpp`. All the JavaScript frontend code is in `web/index.html`.
