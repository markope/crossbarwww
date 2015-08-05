On the Yun:

```console
opkg update
opkg install node
opkg install node-serialport
```

On the PC:

```console
mkdir -p /tmp/yun
cd /tmp/yun
npm install arduino-firmata
npm install autobahn
rm -rf node_modules/arduino-firmata/node_modules/serialport/
scp -r ./node_modules/* root@192.168.1.141:/usr/lib/node_modules
```


```javascript
console.log("blinky starting ..");

var firmata = require('arduino-firmata');
var arduino = new firmata().connect('/dev/ttyATH0');

console.log("libraries loaded.");

arduino.on('connect', function () {
  console.log("serial connected: " + arduino.serialport_name);
  console.log("board version: " + arduino.boardVersion);

  var stat = true;
  setInterval(function () {
    console.log(stat);
    arduino.digitalWrite(13, stat);
    arduino.digitalWrite(12, !stat);
    stat = !stat;  // blink
  }, 300);
});
```
