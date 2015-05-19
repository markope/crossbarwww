Control your browser remotely via WAMP.

Features

* reload the current page
* navigate to another page
* open a second tab & set its URL

**Reload** enables you to refresh content which is displayed remotely.

**Navigating to another page** allows you to chain content if you can modify all pages to load this control code.

**Open a second tab & set its URL** enables you to sequence arbitrary web pages for display. (This requires allowing pop-ups for the domain the controlled page is served from.)

These features are just a basic set, and can be easily extended to other control should you need this. For example, you could navigate the browser history or even modify page content.

## Try it out

The code for this can be found in the [crossbarexamples GitHub repository](https://github.com/crossbario/crossbarexamples) under `iotcookbook`. You need to clone this (or [download it as a ZIP file](https://github.com/crossbario/crossbarexamples/archive/master.zip)).


Then navigate to 'iotcookbook/device/browser/browserremote' and do

```
crossbar start
```

This will serve a demo page with the sample controls at

```
localhost:8080
```

Then launch the page to control using the provided link.

## The API

**Reload**

```javascript
session.publish("io.crossbar.examples.remotecontrol.on_reload");
```

**Navigate**

```
session.publish("io.crossbar.examples.remotecontrol.on_navigate", [newUrl]);
```

**Open a second tab**

```javascript
session.publish("io.crossbar.examples.remotecontrol.on_navigate_external", [externalUrl]);
```

> Note: A new tab is openend on first call. Subsequent calls change the URL for this tab and do not open additional tabs.

**Close the second tab**

```javascript
session.publish("io.crossbar.examples.remotecontrol.on_close_external");
```

> Note: Since only a single external tab is ever opened, this does not require any arguments to identify the tab to close.


> General Note: The above actions may more naturally be expressed through RPCs. However, with PubSub simultaneous control of multiple displays is possible. I just felt that this beat other considerations. (Alex)

## Using it

Browser remote control requires that you load two JavaScript files in your page:

* AutobahnJS
* remote.js

AutobahnJS provides the WAMP connectivity, while `remote.js` actually establishes the WAMP connection, subscribes to control events and issues commands to the browser.

As is, both `remote.js` and the provided control page assume that they are being served from Crossbar.io, and thus attempt to connect to this IP. Should this not be the case, then you need to adapt both to use the endpoint of the Crossbar.io instance you want to use (i.e. replace the last occurence of `wsuri` in each file with the correct endpoint URL).

> Note: Here AutobahnJS is loaded from our S3 storage. This is provided for development purposes only, and some restrictions regarding download IPs apply. For production, please host your own version!

## Where next

* [Remote control Reveal.js presentations via WAMP](Reveal.js Remote Control)