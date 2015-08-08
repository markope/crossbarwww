These are instructions for creating pressure pads which use pressure-sensitive plastic foil.  For the remarks on the principle of this, see [the 'Weighing Pad' page](Weighing Pad). For an alternative recipe, see [Mini Weight Sensor](Mini Weight Sensor). Feel free to experiment and adapt this for your particular use case.

<div class="topimage_container">
   <img class="topimage" src="../../static/img/iotcookbook/weighingpad/assembly_final.jpg" alt="">   
</div>

## The parts list

Most of what you need to follow along is standard equipment for an electronics hobbyist:

* soldering iron & solder
* scissors and a box cutter
* wire stripper
* gaffer tape
* double-sided duct tape
* some paper

The non-standard ones are:

* the plastic foil (see [sourcing tips](Weighing-Pad#sourcing-the-plastic-foil))
* copper tape
* felt carpet tile 

The felt carpet tile is used to house the actual sensor stack, and to effect some distribution of weight to the sensor stack. The distributionis enough to detect pressure outside of the actual sensor area, but not enough to detect it across the entire surface of the pad.

In principle, there are lots of suitable materials - the stiffer the more even the distribution of the pressure. So before going out and buying carpet tiles (which is just what we had at hand), see what's lying around and might work. After all, experimentation with this part is trivially easy. 

## The instructions

The sensor stack is contained between two segments of gaffer tape. 

We cut these and place them with the non-stick side down. All other pieces of the assembly will be smaller than this, so make sure it's sufficiently large. Trimming this at the end is trivial.

![](/static/img/iotcookbook/weighingpad/gaffer_02.jpg)

We stick a piece of paper on each of the pieces of gaffer tape.

![](/static/img/iotcookbook/weighingpad/paper.jpg)

We use copper tape to get current running the plastic sheeting. The copper tape has a width of 25mm and electrically conductive glue on one side. As mentioned earlied, glue within the sensor stack itself is your enemy, so we won't use this to glue the tape to the foil. 

We cut out a corner from a section of the tape. The broader part is used for contact with the foil, while we'll attach our wiring to the narrow part. 

![](/static/img/iotcookbook/weighingpad/copper_01.jpg)

We do the above twice, yielding the two electrodes.

![](/static/img/iotcookbook/weighingpad/copper_02.jpg)

Here are the two parts of copper tape as they will be positioned in the sensor stack.

![](/static/img/iotcookbook/weighingpad/copper_03.jpg)

We then solder the connecting wires onto our electrodes. (It's easiest to first put a drop of solder on the tape and then re-heat this while pressing the wire against the drop.)

![](/static/img/iotcookbook/weighingpad/copper_04.jpg)

![](/static/img/iotcookbook/weighingpad/copper_05.jpg)

We glue the electrodes to the paper. 

![](/static/img/iotcookbook/weighingpad/assembly_02.jpg)

We fix the wire with a bit of gaffer tape. 

![](/static/img/iotcookbook/weighingpad/assembly_03.jpg)

We now cut pieces of the plastic sheeting. These should be of a size that they cover the copper tape electrodes, but should ideally not extend beyond the area covered by the paper.

![](/static/img/iotcookbook/weighingpad/foil.jpg)

The sensor works with a single layer of plastic, but adding more layers increases the resistance and the dynamic range.

![](/static/img/iotcookbook/weighingpad/assembly_05.jpg)

We fix the foil with some tape (this is one obvious place for optimization).

![](/static/img/iotcookbook/weighingpad/assembly_06.jpg)

We stick the two parts together to form the sensor.

![](/static/img/iotcookbook/weighingpad/assembly_07.jpg)

The sensor after some trimming of the gaffer tape.

![](/static/img/iotcookbook/weighingpad/assembly_08.jpg)

We want a case for the sensor. Here we use a piece of carpet tile. This is stable enough to spread pressure on it to the sensor at this size (and it's what we had at hand). 

![](/static/img/iotcookbook/weighingpad/assembly_09.jpg)

We use double-side duct tape to fix the two pieces of tile together: Cover the entire surface of one tile with the tape. Stick on the sensor. Put tape across the sensor. Stick on the second tile.

![](/static/img/iotcookbook/weighingpad/assembly_10.jpg)

![](/static/img/iotcookbook/weighingpad/assembly_11.jpg)

![](/static/img/iotcookbook/weighingpad/assembly_12.jpg)

![](/static/img/iotcookbook/weighingpad/assembly_13.jpg)

![](/static/img/iotcookbook/weighingpad/assembly_14.jpg)

The finished weighing pad.

![](/static/img/iotcookbook/weighingpad/assembly_final.jpg)

To test the sensor, you can use a common multi meter and measure the resistance. 


## Connecting this to the world

To connect this to the world, you need to connect it some device with connectivity. We currently offer instructions for how to do this using an Arduino yun, with the aid of some resistors and a bit more work with the soldering iron.

See [Arduino Yun Weighing Pad](Arduino Yun Weighing Pad)
