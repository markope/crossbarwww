This page contains instructions for how to exand the disk space available on the Yun using a microSD card. The Yun itself has only 16MB of flash, and half of that is reserved as a recovery partition. 

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

Hence we will create a new filesystem on a micro SD card which we can use for both programs and data and mount that filesystem as an overlay on top of the root directory (usually, this is called an "extroot").

We suggest formatting the entire SD card with a single partition, since otherwise the steps below may lead to only part of the card's capacity being accessible.

This is what the filesystem looks like after exanding (using a 1GB SD card):

```shell
root@Arduino:~# df -h
Filesystem                Size      Used Available Use% Mounted on
rootfs                  816.7M      3.0M    771.4M   0% /
/dev/root                 7.0M      7.0M         0 100% /rom
tmpfs                    29.9M    104.0K     29.8M   0% /tmp
tmpfs                   512.0K         0    512.0K   0% /dev
/dev/sda2               816.7M      3.0M    771.4M   0% /overlay
overlayfs:/overlay      816.7M      3.0M    771.4M   0% /
/dev/sda1                99.8M      4.0K     99.8M   0% /mnt/sda1
```

There is an [official tutorial](http://arduino.cc/en/Tutorial/ExpandingYunDiskSpace) for the disk expansion. However, the process there has proven to be quite brittle (we go about 20% success rate). So here's an alternative way.

The following can be pasted into your remote shell on the Yun as is block-by-block. However, you may want to take the time to paste them line-by-line since this makes it easier to find where a problem lies should any occur.

* install the required tools:
```shell
opkg update
opkg install e2fsprogs mkdosfs fdisk rsync
```
* erase the partition table
```shell
dd if=/dev/zero of=/dev/sda bs=4096 count=1000
```
* create an Ext4 partition
```shell
(echo o; echo n; echo p; echo 1; echo ; echo; echo w) | fdisk /dev/sda
```
* format the partition
```shell 
umount /dev/sda1
mkfs.ext4 /dev/sda1
```
* copy files from the Yun flash to the card
```shell
mkdir -p /mnt/sda1
mount /dev/sda1 /mnt/sda1
rsync -a --exclude=/mnt/ --exclude=/www/sd /overlay/ /mnt/sda1/
umount /dev/sda1
rm -rf /mnt/sda1
```
* enable the card as additional disk space
```shell
uci add fstab mount
uci set fstab.@mount[0].target=/overlay
uci set fstab.@mount[0].device=/dev/sda1
uci set fstab.@mount[0].fstype=ext4
uci set fstab.@mount[0].enabled=1
uci set fstab.@mount[0].enabled_fsck=0
uci set fstab.@mount[0].options=rw,sync,noatime,nodiratime
uci commit
```
* reboot the Yun

## Next steps

Install the software to remote control the Yun's Arduino pins.

* [Remote Control](Arduino-Yun-Remote-Control)
