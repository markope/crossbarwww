This recipe describes how to create a SD card for the Yun with all our software and to be used as a root overlay on the Yun ("extroot"). Users then can simply use this image for quick start.


## Prepare SD card

**You will need a SD card with at least 1GB. Ideally, use a fast card .. class 10.**

We'll be preparing the SD card on a Linux PC, not the Yun, since this is faster.

First, determine the corresponding Linux device for the SD card. 

```console
sudo fdisk -l
```

**You have to be absolutely sure you have the correct device, otherwise you might destroy your system! Also, you have to change the device used in the commands below to match your system! Again, otherwise you might destroy stuff! YOU HAVE BEEN WARNED.**

When using a fresh SD card, it's sufficient to delete any existing partition table:

```console
sudo dd if=/dev/zero of=/dev/sde bs=4096 count=1000
```

When using an already used SD card, make sure to fill it up with zeroes first:

```console
sudo dd if=/dev/zero of=/dev/sde bs=1M count=900
```

Now parition the SD card using the following command. This will create 2 partitions:

1. a FAT32 400MB partition
2. a Ext4 400MB partition

```console
(echo o; echo n; echo p; echo 1; echo; echo +400M; echo n; echo p; echo 2; echo; echo +400M; echo t; echo 1; echo c; echo w) | sudo fdisk /dev/sde
```

> Note that the FAT32 partition MUST be the first partition. Otherwise Windows won't be able to see the partition (Windows only recognizes the first partition on removable storage media)

Now format the partitions:

```console
sudo mkfs.vfat /dev/sde1
sudo mkfs.ext4 /dev/sde2
```

## Update the Yun

Now do an update of the Yun's Linux base image:

```console
opkg update
opkg install unzip
cd /tmp
wget http://downloads.arduino.cc/openwrtyun/1/YunSysupgradeImage_v1.5.3.zip
unzip YunSysupgradeImage_v1.5.3.zip
sysupgrade -v -n openwrt-ar71xx-generic-yun-16M-squashfs-sysupgrade.bin
```

## Activate Extroot

Now insert the previously prepared SD card, copy over the base image files

```console
opkg update
opkg install rsync
mkdir -p /mnt/sda2
mount /dev/sda2 /mnt/sda2
rsync -a --exclude=/mnt/ --exclude=/www/sd /overlay/ /mnt/sda2/
umount /dev/sda2
rm -rf /mnt/sda2
```

activate the overlay:

```console
uci add fstab mount
uci set fstab.@mount[0].target=/overlay
uci set fstab.@mount[0].device=/dev/sda2
uci set fstab.@mount[0].fstype=ext4
uci set fstab.@mount[0].enabled=1
uci set fstab.@mount[0].enabled_fsck=0
uci set fstab.@mount[0].options=rw,sync,noatime,nodiratime
uci commit
```

and reboot.


## Install software

Follow the recipes for

* [Setup Autobahn|Python](Arduino-Yun-AutobahnPython-Setup)
* [Setup Autobahn|JS](Arduino-Yun-AutobahnJS-Setup)

Install some more tools:

```console
opkg update
opkg install git wget curl bzip2 tar unzip nano vim
opkg install openssh-sftp-server
```

## Finalize image

Follow the recipe for

* [Disable the serial bridge](Arduino-Yun-Disable-Bridge)

Then, on the Yun:

```console
rm /etc/extroot.md5sum
```

## Make the image

On the PC, insert the SD card prepared on the Yun and

```console
sudo dd if=/dev/sde of=/tmp/autobahn_yun_extroot.img bs=1M count=900
zip -j -9 /tmp/autobahn_yun_extroot.zip /tmp/autobahn_yun_extroot.img
```

Now upload the image to `https://s3-eu-west-1.amazonaws.com/crossbar.io/download/autobahn_yun_extroot.zip`.

