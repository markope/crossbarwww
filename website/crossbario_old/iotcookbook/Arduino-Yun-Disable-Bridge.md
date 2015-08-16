We are using the serial connection between the MCU and the CPU. By default, there is a console attached on the Linux side to the serial, and we need to disable that.

> Note that doing so will disable the [Arduino Yun Bridge](https://www.arduino.cc/en/Reference/YunBridgeLibrary)

Edit the file `/etc/inittab` and comment the following line (by preceding it with `#`):

```
# ttyATH0::askfirst:/bin/ash --login
```

and reboot

```console
reboot
```

> Be patient, a reboot (either via the `reboot` command like above, or by doing a cold boot via power cycling or pressing the "Yun RST" button) can take 60-90s.
> 

**Background**

The Linux SoC (CPU) and the Atmel MCU are connected via a UART (a serial connection) which maps to the device `/dev/ttyATH0` on the Linux side and the [serial stream](http://arduino.cc/en/Reference/Serial) class `Serial1` on the Arduino side. The default `inittab` entry on the Linux side will start a shell connected to that serial port when Linux boots. Then, when your sketch starts the Arduino Yun bridge library (by doing `Bridge.begin()`), the bridge library writes a command to the serial that will in turn start a script on the Linux side which then connects to the serial port. That Linux script is essentially the Linux-side part of the Yun bridge library and will keep on running regardless of wether you reload a new sketch to the MCU or reset the MCU. It will keep on running until you reset the CPU or reboot Linux (or manually kill the script). However, as long as there is a script running and using the serial port, we cannot use the serial for our purposes. The commenting of the `inittab` line will disable starting a shell on the serial port altogether in the first place. **This means we can use the serial port for our stuff, but it also means you won't be able to use the Yun brigde library anymore.**
> 

## Next

Depending on what language you intend to use on the CPU part of the Yun, please continue

* [Setting up Autobahn|Python](Arduino-Yun-AutobahnPython-Setup)
* [Setting up Autobahn|JS](Arduino-Yun-AutobahnJS-Setup)
