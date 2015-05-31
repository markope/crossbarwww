**--- under construction ---**

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


