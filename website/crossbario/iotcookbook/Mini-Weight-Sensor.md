These are instructions for creating small, extremely simple pressure sensors which use pressure-sensitive plastic foil.  For the remarks on the principle of this, see [the 'Weighing Pad' page](Weighing Pad). For an alternative recipe, see [Pressure Pads](Pressure Pad). Feel free to experiment and adapt this for your particular use case.

<div class="topimage_container">
   <img class="topimage" src="../../static/img/iotcookbook/weighingpad/washer_06.jpg" alt="">   
</div>

## The parts list

Most of what you need to follow along is standard equipment for an electronics hobbyist:

* soldering iron & solder
* scissors and a box cutter
* wire stripper
* ring washers

The non-standard ones are:

* * the plastic foil (see [sourcing tips](Weighing-Pad#sourcing-the-plastic-foil))
* copper tape
* rubber bumper (e.g. for furniture) 

## The instructions

This simple sensor consists of the foil sandwiched between two ring washers. The washers are covered in copper foil. The sensor stack is kept together by two bits of hot-melt glue. The stack is then glued onto a rubber bumper.

Cut a square of foil, with an edge length of the diameter of the ring washer you're using (it's no a problem if it exceeds this a bit - the area of the ring washer is what determines resistance here).

Cut a piece of the copper tape, with one edge longer than the diameter of the ring washer (for the small size washer we're using, about 50% longer).

Stick the washer to the copper tape (we're using self-adhesive tape with conductive adhesive, otherwise try to keep the glue layer as thin as possible).

![](/static/img/iotcookbook/weighingpad/washer_01.jpg)

We want the copper tape to only cover the washer area, since this gives us a standardized area. Cut away the copper tape inside of the ring as well as outside, but leave a tongue for attaching the wire. Solder the wire to the tongue close to the washer, and the fold over the tongue. With the copper tape we're using, the tongue sticks together and forms a pocket protecting the solder point.

![](/static/img/iotcookbook/weighingpad/washer_02.jpg)

We then put together the stack of a layer of foil and two washers. We want as little glue as possible within the stack, since the elasticity of the glue can lead to delayed sensor readings. So until we fix the stack, we need to clip it together. One way of doing this is using crocodile clips.

![](/static/img/iotcookbook/weighingpad/washer_03.jpg)

We then glue to together the stack by applying a bit of hot-melt glue within the inside of the ring washer on both sides. This needs to be done quickly, as there's a danger of melting the plastic foil otherwise. The glue is there to connect to both the foil and the inner sides of the ring washer to give a mechanical connection here. Keep the amount of glue low here - this may not stick out above the level of the washer, since otherwise the glue is what bears the pressure. (If you do apply too much glue, like in the photo below, then you need to scrape the extra off - so better get it right initially!)

![](/static/img/iotcookbook/weighingpad/washer_04.jpg)

The sensor itself is now finished. As an extra step, we add the rubber bumper. 

![](/static/img/iotcookbook/weighingpad/washer_05.jpg)

You can then fix this to the bottom of e.g. a base plate on which to place objects to weigh.

![](/static/img/iotcookbook/weighingpad/washer_06.jpg)

Note:
The initial resistance and the change in this depend on the type of foil used. With the type we had at our disposal, the range was best suited for measuring loads of up to a few kilos. For a sensor which has a wider range see the [Pressure Pad](Pressure Pad).


## Connecting this to the world

To connect this to the world, you need to connect it some device with connectivity. We currently offer instructions for how to do this using an Arduino yun, with the aid of some resistors and a bit more work with the soldering iron.

See [Arduino Yun Weighing Pad](Arduino Yun Weighing Pad)
