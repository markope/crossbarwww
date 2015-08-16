A simple, robust and cheap weight sensor is something which lends itself to many uses, from checking current storage levels of printer paper (packs in the printer room, not sheets in the printer) to dance games or interactive twister.

Here we show how to construct such a weight sensor in two different variants. For connecting it to receive the current data see e.g. the [Arduino Yun Weighing Pad component](Arduino Yun Weighing Pad).

## The principle

Our weighing pad uses the fact that with certain kinds of conductive plastic foil its resistance varies with the pressure applied. One or more pieces of this plastic foil are at the core of our sensor.

The basic construction of the sensor is then to have the plastic foil between two electrodes.

A guiding principle in constructing the sensor is to keep elastic layers to a minimum, especially in the core sensor stack. The compression and decompression of these layers leads to slower pressure changes on the sensor.

## Two recipes

There are many ways of making sensors. (Experimenting with some approaches has given us a deeper appreciationg of what hardware engineers do.) Here we present two recipes that worked for us. These are just suggestions - you can build them as we show it, or you can use them as a starting point for your own experiments. Should you come up with your own version which works well for your use case, then please send us a description which we can add here!

* [The Pad](Pressure Pad) - Felt pads, used in the [Euro Pallet Load App](Euro Pallet Load) 
* [The Mini](Mini Weight Sensor) - About the simplest possible sensor

> Note: The range over which the sensors measure precisely depends in large part on the precise type of foil used. With any of these sensors, you need to perform calibration yourself. We provide calibration tool which collects data for particular loads you want to distinguish - [wpadlab](wpadlab).


## Sourcing the plastic foil

Sourcing the plastic foil may be the hardest part about the recipes, since it is not commonly available. 

We got some from an IoT kit ([plug & wear](http://www.plugandwear.com), PW074, Shaped Analog Sensor Kit).

You can also order larger quantities (a full roll) from a manufacturer, e.g. from [Caplinq](http://www.caplinq.com/electrically-conductive-plastic-film.html).

The vendor has the following to say: [Which Linqstat product is right for pressure sensors? ](http://caplinq.com/blog/which-linqstat-product-is-right-for-pressure-sensors_890/)

In particular:

> The thinner sheets are less sensitive to pressure changes than the thicker ones (because essentially by reducing the thickness, you increase the conductivity). The minimum thickness suitable for pressure sensors is 4mil, but the 6-mil and 8-mil thicknesses are more common for pressure sensors.

More information:

* [Difference in Surface Resistivity of Linqstat Volume Conductive Films ](https://www.youtube.com/watch?v=bX_oo1hr1ag)
* [How to measure surface resistivity of plastic conductive films ](https://www.youtube.com/watch?v=Kl4RpZTfTbI)

## A note on commercial sensors

We found the DIY approach using the resistive foil interesting and something worth experimenting with. We have not tested any commercial sensors. If you use such a sensor, then you may still find components in this cookbook which allow the transmission of sensor values interesting (such as the [Arduino Yun Weighing Pad Component](Arduino Yun Weighing Pad)). It should not be difficult to adapt these to use the sensor you've settled on.