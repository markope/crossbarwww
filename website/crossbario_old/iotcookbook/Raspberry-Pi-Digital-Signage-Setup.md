The easiest way to use the Raspberry Pi for Digital Signage is displaying content in a browser.

The following tutorial describes how to set up a Pi so that it boots directly into Chromium and displays a preset Web page.

This is not WAMP or Crossbar.io related as such. We suggest you load the [browsercontrol component](Browser Remote Control) which allows you to change the displayed pages and/or a [Reveal.js](http://lab.hakim.se/reveal-js/#/) presentation which you can control via the [revealcontrol component](Reveal.js Remote Control).

## Prerequisites

You need a Raspberry Pi with Raspian installed. We suggest using a second-generation model, since this has significantly more processing power than the first generation, and enables you to run more complex pages in the browser.

## Fixing the overscan problem

You will most likely connect the Pi to a display using the HDMI port. With a standard configuration, overscan is still enabled, leaving a black border at the sides of the display (since you might connect the Pi to a CRT). In order to fix this, you need to edit `boot/config.txt`. This is easiest done by doing 

```
sudo nano /boot/config.txt
```

which starts the nano editor with the file.

In the file, `disable_overscan=1` needs to be set. This will usually be commented out. Uncomment this, or add it. Also make sure that there are no additional configuration options for overscan set - it's best to scan the entire config file until the end. (When [NOOB]() was used for setup, this adds more configuration at the end which needs to be removed.)

## Setting up the Pi

The following steps are based on an [excellent blog post](http://blogs.wcode.org/2013/09/howto-boot-your-raspberry-pi-into-a-fullscreen-browser-kiosk/). The main reason for not only including the link is to have the information right here and prevent linkrot from making this useless.

### Initial setup

You need to install some additional software. Do

```bash
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install matchbox chromium x11-xserver-utils ttf-mscorefonts-installer xwit sqlite3 libnss3
sudo reboot
```

### Automatic resolution detection

This is only necessary if you the Pi may connect to displays of different resolution. Otherwise just set the correct resultion for the display you are using once and skip this step!

This solution starts off by setting the internal framebuffer to its maximum (1900 x 1200) and then adjusting downward to the actual display's resolution if necessary.

Add the following to `/boot/config.txt`

```
# 1900x1200 at 32bit depth, DMT mode
disable_overscan=1
framebuffer_width=1900
framebuffer_height=1200
framebuffer_depth=32
framebuffer_ignore_alpha=1
hdmi_pixel_encoding=1
hdmi_group=2
```

Then add the following to `/etc/rc.local`

```
# Wait for the TV-screen to be turned on...
while ! $( tvservice --dumpedid /tmp/edid | fgrep -qv 'Nothing written!' ); do
   bHadToWaitForScreen=true;
   printf "===> Screen is not connected, off or in an unknown mode, waiting for it to become available...\n"
   sleep 10;
done;

printf "===> Screen is on, extracting preferred mode...\n"
_DEPTH=32;
eval $( edidparser /tmp/edid | fgrep 'preferred mode' | tail -1 | sed -Ene 's/^.+(DMT|CEA) \(([0-9]+)\) ([0-9]+)x([0-9]+)[pi]? @.+/_GROUP=\1;_MODE=\2;_XRES=\3;_YRES=\4;/p' );

printf "===> Resetting screen to preferred mode: %s-%d (%dx%dx%d)...\n" $_GROUP $_MODE $_XRES $_YRES $_DEPTH
tvservice --explicit="$_GROUP $_MODE"
sleep 1;

printf "===> Resetting frame-buffer to %dx%dx%d...\n" $_XRES $_YRES $_DEPTH
fbset --all --geometry $_XRES $_YRES $_XRES $_YRES $_DEPTH -left 0 -right 0 -upper 0 -lower 0;
sleep 1;
```


### Launching Chromium

We want to launch Chromimum on startup, with any changes users might have made in the interim reverted. We also want to display a start page we configure.

Add this to `/etc/rc.local`:

```
if [ -f /boot/xinitrc ]; then
   ln -fs /boot/xinitrc /home/pi/.xinitrc;
   su - pi -c 'startx' &
fi
```

You then need to create `/boot/xinitrc` with the following contents:

```
#!/bin/sh
while true; do

   # Clean up previously running apps, gracefully at first then harshly
   killall -TERM chromium 2>/dev/null;
   killall -TERM matchbox-window-manager 2>/dev/null;
   sleep 2;
   killall -9 chromium 2>/dev/null;
   killall -9 matchbox-window-manager 2>/dev/null;

   # Clean out existing profile information
   rm -rf /home/pi/.cache;
   rm -rf /home/pi/.config;
   rm -rf /home/pi/.pki;

   # Generate the bare minimum to keep Chromium happy!
   mkdir -p /home/pi/.config/chromium/Default
   sqlite3 /home/pi/.config/chromium/Default/Web\ Data "CREATE TABLE meta(key LONGVARCHAR NOT NULL UNIQUE PRIMARY KEY, value LONGVARCHAR); INSERT INTO meta VALUES('version','46'); CREATE TABLE keywords (foo INTEGER);";

   # Disable DPMS / Screen blanking
   xset -dpms
   xset s off

   # Reset the framebuffer's colour-depth
   fbset -depth $( cat /sys/module/*fb*/parameters/fbdepth );

   # Hide the cursor (move it to the bottom-right, comment out if you want mouse interaction)
   xwit -root -warp $( cat /sys/module/*fb*/parameters/fbwidth ) $( cat /sys/module/*fb*/parameters/fbheight )

   # Start the window manager (remove "-use_cursor no" if you actually want mouse interaction)
   matchbox-window-manager -use_titlebar no -use_cursor no &

   # Start the browser (See http://peter.sh/experiments/chromium-command-line-switches/)
   chromium  --app=http://URL.of.your/choice.html

done;
```


Be aware that even on a second-generation Pi, the full boot process takes a while - so be patient before deciding that you made a mistake somewhere along the way.

The boot process erases any user changes since the last boot, so this should be OK for public usage. Of course, if you only need this as digital signage, just don't attach a mouse or keyboard!


## Components to load

If you want to control what the browser displays, we currently offer two components which both utilize WAMP connections:

* [browserremote](Browser Remote Control) which allows you to control the contents of another tab (i.e. you can display arbitrary web pages), as well as reloading the current tab or navigating away from it. (There is a problem with Chromium opening a new tab in a separate Window, so if you want to use this feature a bit of manual setup is required after startup.)
* [revealremote](Reveal.js Remote Control) which allows you to remote control a [Reveal.js](http://lab.hakim.se/reveal-js/#/) presentation. These are authored in HTML, and offer you the full power of the browser in your presentations.
