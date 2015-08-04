This page contains instructions for how to exand the disk space available on the Yun using a microSD card.  For an overview of all materials we have concerning the Yun, please see [here](Arduino Yun).

## Links

* http://wiki.openwrt.org/doc/howto/extroot
* http://wiki.openwrt.org/doc/howto/extroot/extroot.theory
* http://blog.lincomatic.com/?p=1287
* https://samhobbs.co.uk/2013/11/more-space-for-packages-with-extroot-on-your-openwrt-router

## The disk space problem

The Yun itself has only 16MB of flash, and half of that is reserved as a recovery partition.

```shell
root@Arduino:~# df -h
Filesystem                Size      Used Available Use% Mounted on
rootfs                    7.5M    392.0K      7.1M   5% /
/dev/root                 7.0M      7.0M         0 100% /rom
tmpfs                    29.9M    344.0K     29.5M   1% /tmp
tmpfs                   512.0K         0    512.0K   0% /dev
/dev/mtdblock3            7.5M    392.0K      7.1M   5% /overlay
overlayfs:/overlay        7.5M    392.0K      7.1M   5% /
```

The free space on this is not enough for the software we want to install.

## Using a microSD for storage

Hence we will create a new filesystem on a micro SD card which we can use for both programs and data and mount that filesystem as an overlay on top of the root directory (called [extroot](
http://wiki.openwrt.org/doc/howto/extroot)).

We suggest formatting the entire SD card with a single partition, since otherwise the steps below may lead to only part of the card's capacity being accessible.

## The official way

There is an [official tutorial](http://arduino.cc/en/Tutorial/ExpandingYunDiskSpace) for the disk expansion. However, the process there has proven to be quite brittle (we go about 20% success rate). So here's an alternative way.

## Our way

Insert a SD card (at least 1GB recommended) and run the following on the Yun:

```console
# install required tools
opkg update
opkg install e2fsprogs mkdosfs fdisk rsync

# erase the partition table
dd if=/dev/zero of=/dev/sda bs=4096 count=1000

# create an Ext4 partition
(echo o; echo n; echo p; echo 1; echo ; echo; echo w) | fdisk /dev/sda

# format the partition
umount /dev/sda1
mkfs.ext4 /dev/sda1

# copy files from the Yun flash to the card
mkdir -p /mnt/sda1
mount /dev/sda1 /mnt/sda1
rsync -a --exclude=/mnt/ --exclude=/www/sd /overlay/ /mnt/sda1/
umount /dev/sda1
rm -rf /mnt/sda1

# enable the card as additional disk space
uci add fstab mount
uci set fstab.@mount[0].target=/overlay
uci set fstab.@mount[0].device=/dev/sda1
uci set fstab.@mount[0].fstype=ext4
uci set fstab.@mount[0].enabled=1
uci set fstab.@mount[0].enabled_fsck=0
uci set fstab.@mount[0].options=rw,sync,noatime,nodiratime
uci commit
```

The reboot the Yun. After rebooting, this is what the filesystems looks (using a 1GB SD card):

```shell
root@Arduino:~# df -h
Filesystem                Size      Used Available Use% Mounted on
rootfs                  943.6M     31.2M    865.1M   3% /
/dev/root                 7.5M      7.5M         0 100% /rom
tmpfs                    29.8M    100.0K     29.7M   0% /tmp
tmpfs                   512.0K         0    512.0K   0% /dev
/dev/sda1               943.6M     31.2M    865.1M   3% /overlay
overlayfs:/overlay      943.6M     31.2M    865.1M   3% /
```

## Next

The microcontroller and CPU on the Yun are connected over a on-board serial connection. However, the connection is already used by some software, and we need to disable that to use the serial connection for our own purposes. Head over to:

* [Disable Serial Bridge](Arduino-Yun-Disable-Bridge)
