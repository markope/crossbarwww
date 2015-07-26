The Arduino Yun Weighing Pad component publishes data from a weighing pad component (see [instructions for making these](Weighing Pad)). It can publish both raw data and events when certain configurable thresholds are passed. 

## The sensor

The [weighing pad sensor](Weighing Pad) uses a type of plastic foil which changes resistance in reaction to pressure. It is a simple DIY project, consists of low-cost components, and can be made reasonably robust very easily.

<div class="topimage_container">
   <img class="topimage" src="../../static/img/iotcookbook/weighingpad_arduino_yun.png" alt="">   
</div>

## Trying it out

### Hardware

Using an Arduino XXX shield, here are step-by-step instructions:


--- add instructions for connecting the sensors ---
--- ask Tobias ---


### Software

The code for this can be found in the [crossbarexamples GitHub repository](https://github.com/crossbario/crossbarexamples) under `iotcookbook`. You need to clone this (or [download it as a ZIP file](https://github.com/crossbario/crossbarexamples/archive/master.zip)).

Open a shell in the component directory (crossbarexamples/iotcookbook/device/yun/weighingpad).

Start up Crossbar.io:

```shell
crossbar start
```

This also serves a frontend where you can view the weighing pad data logged at

```
http://localhost:8080
```

#### Configuration

In `weighingpad_yun.js`, add the URL of the machine on which Crossbar.io runs:

```javascript
var connection = new autobahn.Connection({
   url: "ws://<URL OF YOUR CROSSBAR INSTANCE>/ws", // replace with the url of your crossbar instance
   realm: "iot_cookbook"
});
```

You **need** to have completed the **setup for remote GPIO access** on the Yun - see [[Arduino Yun Remote GPIO]], and have at least one weighing pad connected.

The general configuration for the component is:

   * the pins to which weighing pads are connected
   * an id for the Yun which is used for the publication topic or sent as part of the data
   * the sampling frequency (how many milliseconds pass between polling for values)
   * whether data is sent continuously or only if there has been a value change

The configuration is in the `config` variable, and as a default raw data is published every 200 milliseconds.

The component has two main modes for sending sensor data:

* raw data
* changes in user-defined units

With **raw data**, the component just sends the current sensor readings. If you have the component set to publish data only on value changes, then you additionally need to configure how big the value change has to be (on a per-sensor basis) to trigger the sending.

With **changes in user-defined units**, only a single unit value is transmitted which is determined by the component across all sensor readings. You provide training data, i.e. sets of sensor readings (like raw mode delivers) together with a value which these correspond to. The component then determines which which set the current readings are closest to and sends this change.

For creating the sets of sensor readings, you can use the [wpadlab](Wpadlab).

Once you've got things configured, transfer `weighingpad_yun.js` to the Yun, e.g. by doing 


```shell
scp weighingpad_yun.js root@<IP of your Yun>:~/
```

in the component directory.

Then run the file on the Yun.

```shell
node weighingpad_yun.js
```

which should log something like

```shell
Arduino Yun Weighing Pads starting ...
Arduino connected (over /dev/ttyATH0, board version 2.3)
Connecting to router ...
/usr/bin/nodejs: '/usr/lib/node_modules/autobahn/node_modules/ws/node_modules/bufferutil/build/Release/bufferutil.node' is not an ELF file
/usr/bin/nodejs: '/usr/lib/node_modules/autobahn/node_modules/ws/node_modules/utf-8-validate/build/Release/validation.node' is not an ELF file
Router connected. Session ID: 1311074825864401
setting mode for pin 1
setting mode for pin 2
publishing:  { '1': 992, '2': 1001 }
```

In the above example, two weighing pads are connected (pins 1 & 2).

### The API

The components publishes the current weighing pad data as an event

```
io.crossbar.examples.yun.weighingpad.on_sample
```

The payload is an object, e.g. 


```javascript
{
   id: "yun1",
   samples: {
      1: 345,
      2: 999
   }
}
```

and the frequency of publication depends on the configuration.

To allow retrieval of the configuration, the component subscribes to

```
io.crossbar.examples.yun.weighingpad.who_is_out_there
```

and responds with a publication to 

```
io.crossbar.examples.yun.weighingpad.i_am_here
```

which contains its configuration as the payload, e.g.

```javascript
{
   id: "yun1",
   pins: [1, 2],
   frequency: 200,
   publishOnDifference: false
}
```

To change the configuration, the component registers a procedure, e.g.

```
io.crossbar.examples.yun.weighingpad.yun1.configure
```

which can be called with any subset of confguration values, e.g.

```
{
   id: "parkingSpace_01"
}
```

to change the ID contained in the values event to, and to which the yun responds to "parkingSpace_01". (This results in a de-registration and re-registration of the configuration procedure, which would now be reachable under `io.crossbar.examples.yun.weighingpad.parkingSpace_01.configure`.), or

```
{
   frequency: 10,
   publishOnDifference: true,
   difference: 100
}
```

which would switch the sending of events from a constant stream (at the sampling frequency) to events only sent when there are value changes which exceed the difference threshold (set here to `100`), as well as setting a new sampling frequency.



--------------- Advanced version - work in progress ----------------

You can additionally configure

* the data transmission frequency (for the default continuos transmission)
* thresholds per-pad
* whether threshold-events or continuos transmission is used per pad

An example configuration is:

```javascript
var config = {
   instance: "yun1",
   pads: [
      {
         pin: 1,
         type: continuous,
         frequency: 1000
      },
      {
         pin: 2,
         type: continuous,
         frequency: 50
      },
      {
         pin: 3,
         type: threshold,
         frequency: 1
         thresholds: {
            emtpy:  {
               min: 0,
               max: 5,
               duration: 1000
            },
            permanent: {
               min: 23,
               max: 100,
               duration: 1000
            },
            impulse: {
               min: 60,
               max: 100,
               duration: 0
            }
         }
      }
   ]
];
```

In the above configuration, the yun sending the data is identified by the instance name. Three weighing pads are connected. 

The first weighing pad connected to pin  1 sends its current value every second (1000 ms), which is useful if you only need to check for more permanent pressure changes, e.g. whether a car is parked or not. 

With the second pad, connected to pin 2 the sampling frequency is 50 ms, allowing more fine-grained detection of pressure changes. 

For the third pad, connected to pin 3, events are produced if: the pressure is a value between 0 and 5% of the configured range and this persists for at least 1 second ("empty"), if the pressure is between 23% and 100% and this persists for at least 1 s ("permanent"), and if the pressure is above 60% for even a single sample ("impulse"). The sampling frequency for events is set to 1 ms.

--- do we need to configure a range per pad? test this! ---

If all you set is the pin, then the component defaults to continuous transmission with a sampling frequency of 100ms. 

If you have a pad connected but do not wish to receive data or events for it, then set the type to `none`. 

The configuration can be changed via WAMP calls during operation (see below).

Transfer `weighingpad_yun.js` on the Yun, e.g. by doing 

```console
scp weighinpad_yun.js root@<IP of your Yun>:~/
```

Then run `weighingpad_yun.js` 

```shell
node weighingpad.js
```

This should log something like

```shell
Arduino Yun Weighingpad starting ...
Arduino connected (over /dev/ttyATH0, board version 2.3)
Connecting to router ...
Router connected. Session ID: 1595783623
```

Once this is running, open the browser console for the frontend page. You'll see data and evnets logged as they are received, e.g. for a single weighing pad at the default continuos transmission.

```javascript
received weighingpad sample data: yun1, pin 1, value 2
received weighingpad sample data: yun1, pin 1, value 1
received weighingpad sample data: yun1, pin 1, value 2
```

### The API

The component publishes two types of events: continuous sampling events and treshold events:

```
io.crossbar.examples.yun.weighingpad.on_sample
io.crossbar.examples.yun.weighingpad.on_event
```

Sample events have the structure:

{ 
   instance: "yun1"
   pin: 1,
   value: 34
}

Threshold events have the structure:

{
   instance: "yun1"
   pin: 4,
   name: "impulse"
}

It also registers two procedures:

```
io.crossbar.examples.yun.weighingpad.<instance_name>.get_config
```

which returns the current configuration and

```
io.crossbar.examples.yun.weighingpad.<instance_name>.update_config
```

which can be called to update the current configuration. 

The call takes a dictionary of the same format as the config. As an example, assume the following dictionary were sent to an instance currently configured as "yun1" with the configuration listed earlier in this documentation:

var config = {
   instance: "my_yun_3",
   pads: [
      {
         pin: 1,
         type: none
      },
      {
         pin: 3,
         type: threshold,
         frequency: 1
         thresholds: {
            emtpy:  none,
            permanent: {
               duration: 500
            },
            transient: {
               min: 50,
               max: 100,
               duration: 50
            }
         }
      },
      {
         pin: 5,
         type: continuous,
         frequency: 1
      }
   ]
];

This accomplished the following changes:

* The pad connected to pin 1 no longer transmits any data.
* The pad connected to pin 3 no longer transmits an "empty" event, the duration of pressure needed to trigger the "permanent" threshold event is lowered to 500ms, and a new threshold event "transient" is added.
* The pad connected to pin 5 now transmits continuos sampling data at a sampling frequency of 1 ms.

   

--------------------

## Assembly

Each **Weighing Pad** station consists of an Arduino Yun with 6 pluggable weighing pads, and each weighing pad has 2 pressure sensors and 1 RGB LED.

## Conductive Plastic

We are using [Linqstat Electrically Conductive Film](http://www.caplinq.com/electrically-conductive-plastic-film.html) for our pressure sensors.

We have settled on using a product from the [LINQSTAT Mid-Level (<= 50,000 ohms/sq) Electrically Conductive Film (LINQSTAT MVCF S-Series)](http://www.caplinq.com/index.php?option=com_virtuemart&Itemid=102&category_id=14&lang=en&page=shop.product_details&product_id=603).

The two products we considered are:

* [MVCF-80012BT10KS/2](http://www.caplinq.com/8-mil-linqstat-mid-level-electrically-volume-conductive-plastic-antistatic-sheeting-12-in.-roll-mvcf-80012bt10ks/2.html)
* [MVCF-40012BT50KS/2](http://www.caplinq.com/4-mil-linqstat-mid-level-electrically-volume-conductive-plastic-antistatic-sheeting-12-in.-roll-mvcf-40012bt50ks/2.html)

The vendor has the following to say: [Which Linqstat product is right for pressure sensors? ](http://caplinq.com/blog/which-linqstat-product-is-right-for-pressure-sensors_890/)

In particular:

> The thinner sheets are less sensitive to pressure changes than the thicker ones (because essentially by reducing the thickness, you increase the conductivity). The minimum thickness suitable for pressure sensors is 4mil, but the 6-mil and 8-mil thicknesses are more common for pressure sensors.

More information:

* [Difference in Surface Resistivity of Linqstat Volume Conductive Films ](https://www.youtube.com/watch?v=bX_oo1hr1ag)
* [How to measure surface resistivity of plastic conductive films ](https://www.youtube.com/watch?v=Kl4RpZTfTbI)

## Copper Foil

It's critical that the copper foil used has an electrically conductive adhesive.

## BOM

* 1 x Arduino Yun, e.g. [this](http://store.arduino.cc/product/A000008) or [this](http://www.watterott.com/de/Arduino-YN?x48ce9=077c146c45b200611345e63c1dfee09c) - **60 Euro**
* 1 x Micro-USB power supply, 5V / 2A, e.g. [this](http://www.amazon.de/Steckernetzteil-Micro-USB-2000mA-Raspberry-Banana/dp/B00EZ5Z2JK) or [this](http://www.amazon.de/Industrie-Standard-Steckernetzteil-HNP13-2USB-schwarz/dp/B00M4CPTYE) - **10 Euro**
* 1 x [Copper foil tape](http://www.adafruit.com/products/1127) - **15 Euro**
* 1 x [Pressure-Sensitive Conductive Sheet (Velostat/Linqstat)](http://www.adafruit.com/products/1361), e.g. [here](http://www.caplinq.com/linqstat-antistatic-electrically-conductive-sheeting-linqstat-vcf-s-series.html), in particular [this](http://www.caplinq.com/2-mil-linqstat-low-level-electrically-volume-conductive-antistatic-plastic-sheeting-12-inch-roll-vcf-20012s/2.html) - **25 Euro**
* 6x Mini-DIN jacket, 6 pol., e.g. [this](http://www.conrad.de/ce/de/product/741797/Mini-DIN-Einbaubuchse-geschirmt-geschirmt-Pole-6-ASSMANN-WSW-Inhalt-1-St) or [here](http://www.reichelt.de/Mini-DIN-Einbaubuchsen/EB-DIOS-M06V/3/index.html?&ACTION=3&LA=2&ARTICLE=52029&GROUPID=5185&artnr=EB-DIOS+M06V) or [here](http://www.amazon.de/20pcs-Tastatur-polige-DIN-Buchse-Stecker/dp/B00UONJKFO) - **10 Euro**
* 6x Mini-DIN cable, 6 po., e.g. [this](http://www.conrad.de/ce/de/product/601847/Miniatur-DIN-Rundsteckverbinder-Stecker-gerade-Polzahl-6-Violett-BKL-Electronic-204097-1-St/) or [here](http://www.amazon.de/Intos-Premium-Kabel-mDIN6-Stecker/dp/B000L0Y33E) - **25 Euro**
* 6 x [NeoPixel Jewel](http://www.adafruit.com/products/2226) - **30 Euro**
* 1 x Breadboard, e.g. [this](http://www.amazon.de/Vktech-Lochrasterplatte-Lochrasterplatine-Leiterplatte-Streifenraster/dp/B00KAPF3Z2) - **5 Euro**
* 1 x Headers, e.g. [this](http://www.amazon.de/SODIAL-Stueck-Gerade-Einreihige-Leiterplatten-Stiftleisten/dp/B00IIDXBXE/) - **4 Euro**

Total BOM: **180 Euro**.

## Connectivity

The 6 weighing pads are connected to the base station over 6 cables using Mini-DIN. Each cable has 6+1 poles:

* GND
* 5V
* Digital Out 1 (for LED)
* Analog IN 1 - 4 (for pressure sensors)


