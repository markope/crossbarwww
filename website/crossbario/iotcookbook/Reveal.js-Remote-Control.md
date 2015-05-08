Control a Reveal.js presentation remotely via WAMP.

## What is Reveal.js?

[Reveal.js]() is probably the most well-established library for HTML5 presentations. Presentations run in the browser, so that no special runtime is needed. Reveal.js has an impressive set of graphical effects out of the box, and you can extend this using the full set of browser technologies.

## Try it out

Get the [Crossbarexamples git repository]().

Then navigate to 'iotcookbook/device/browser/revealremote' and do

```
crossbar start
```

This will serve a demo page with some sample controls at

```
localhost:8080
```

Then open the provided sample presentation using the link in the first line of the control page.

In addition to the on-screen buttons, this handles "PGUP", "PGDOWN" and "." for "previous", "next" and "pause" respectively. These are also the button presses sent by common presentation remote controls (which usally simply register as a keyboard), so that you can use one of these.

## The API

The API consists of two topics:

For navigation there is

```
session.publish('io.crossbar.revealremote.navigate', [action]);
```

where `action` is one of

* `prev` - previous slide/frament
* `next` - next slide/fragment
* `left` - previous slide in horizontal arrangement
* `right` - next slide in horizontal arrangement
* `up` - upwards one slide in vertical arrangement
* `down` - downwards one slide in vertical arrangement
* `first_slide` - display first slide of presentation
* `pause` - pause presentation (blank screen)

For setting auto play options there's

```
sesion.publish('io.crossbar.revealremote.update_autoplay', [delay, loop]);
```

where `delay` is the delay between automatic slide changes in milliseconds and `loop` is a Boolean which indicates whether to start over at the end of the presentation.

Setting `delay` to `0` stops auto play.

This should cover the most common actions needed. It is easy to extend this to cover the rest of the Reveal.js API.

> General Note: The above actions may more naturally be expressed through RPCs. However, with PubSub simultaneous control of multiple displays is possible. I just felt that this beat other considerations.

## Using it

Remote control requires loading two additional JavaScript files in your Reveal.js presentation:

* AutobahnJS
* revealremote.js

AutobahnJS provides the WAMP connectivity, while `revealremote.js` actually establishes the WAMP connection, subscribes to control events and issues commands to Reveal.js.

This presently contains just basic navigation commands plus setup for autoplay, but can be trivially extended to support the entire Reveal.js API.

As is, both `revealremote.js` and the provided control page assume that they are being served from Crossbar.io, and thus attempt to connect to this IP. Should this not be the case, then you need to adapt both to use the endpoint of the Crossbar.io instance you want to use (i.e. replace the last occurence of `wsuri` in each file with the correct endpoint URL).

> Note: Here AutobahnJS is loaded from our S3 storage. This is provided for development purposes only, and some restrictions regarding download IPs apply. For production, please host your own version!

## Links

* [Reveal.js](https://github.com/hakimel/reveal.js/)
* [remote control webpage content via WAMP](https://github.com/crossbario/crossbarexamples/tree/master/browserremote) - combine this with the reveal control to e.g. do playlists of presentations, or presentations with other web content 