Once that you have [networking running for your Yun](Arduino Yun Network Access) (either ethernet, Wifi or both), the next thing is to SSH into your Yun. This will allow you to do further software setup and advanced system configuration from a root shell.

> Note: -nix systems should come with ssh preinstalled. On Windows, git installs an ssh client which you can use from the git shell - or you can use [Putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html). 

The default password for `root` is `arduino`. (Don't be surprised if there's no cursor movement on entering the password - -nix systems have this as a safety feature.)

Here is how that looks like on a first connect:

```console
$ ssh -l root 192.168.1.150
The authenticity of host '192.168.1.150 (192.168.1.150)' can't be established.
RSA key fingerprint is f9:e0:1e:bd:bb:f9:e1:33:5b:c7:5d:75:da:2c:20:b1.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '192.168.1.150' (RSA) to the list of known hosts.
root@192.168.1.150's password:


BusyBox v1.19.4 (2013-08-07 16:16:02 CEST) built-in shell (ash)
Enter 'help' for a list of built-in commands.

      ___                   ___                       ___           ___
     /\__\      ___        /\__\          ___        /\__\         /\  \
    /:/  /     /\  \      /::|  |        /\  \      /::|  |       /::\  \
   /:/  /      \:\  \    /:|:|  |        \:\  \    /:|:|  |      /:/\:\  \
  /:/  /       /::\__\  /:/|:|  |__      /::\__\  /:/|:|  |__   /:/  \:\  \
 /:/__/     __/:/\/__/ /:/ |:| /\__\  __/:/\/__/ /:/ |:| /\__\ /:/__/ \:\__\
 \:\  \    /\/:/  /    \/__|:|/:/  / /\/:/  /    \/__|:|/:/  / \:\  \ /:/  /
  \:\  \   \::/__/         |:/:/  /  \::/__/         |:/:/  /   \:\  /:/  /
   \:\  \   \:\__\         |::/  /    \:\__\         |::/  /     \:\/:/  /
    \:\__\   \/__/         /:/  /      \/__/         /:/  /       \::/  /
     \/__/                 \/__/                     \/__/         \/__/

            _______                     ________        __
           |       |.-----.-----.-----.|  |  |  |.----.|  |_
           |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
           |_______||   __|_____|__|__||________||__|  |____|
                    |__| W I R E L E S S   F R E E D O M

root@Arduino:~#
```

To change the password for `root`, type `passwd`.


#### Public Key Authentication

Now, retyping your password each time you log in gets old fast. Public key based authentication for SSH allows you to do password-less, but nevertheless secure logins.

This isn't the place to give an introduction to SSH and public key authentication, however you should have little problems finding tutorials and information on the net. I will only cover stuff that is "unusual" on the Yun compared to a commonly seen Unix.

The Linino/OpenWRT Linux on the Yun does use Dropbear for SSH support (both client and server) - this is a different software package from usual Linux distributions and Unix systems (which is OpenSSHd).

One difference is that to enable public key based authentication for root, the authorized public keys need to be added to the following file (and not the usual `/root/.ssh/authorized_keys`):

```text
vi /etc/dropbear/authorized_keys
chmod 0600 /etc/dropbear/authorized_keys
```

A complete tutorial for setting up public key based authentication on OpenWRT can be found [here](http://wiki.openwrt.org/oldwiki/dropbearpublickeyauthenticationhowto).


#### SSHFS

Another thing you probably want to do: mount the Yun's filesystem on your desktop via SSH.

Why is that? Mounting over SSH allows you to edit files on the Yun using your favorite editor directly *on your desktop*. So you don't need to fiddle with **vi** and such inside a shell;)

This magic works via SFTP (secure FTP), which is a FTP-like protocol that runs over SSH. On the Yun side, you'll need to have the SFTP package installed, login via SSH as root and do:

```console
opkg update
opkg install openssh-sftp-server
```

Now, on **Windows**, [Win-SSHFS](http://code.google.com/p/win-sshfs/) which you can download from [here](http://code.google.com/p/win-sshfs/downloads/detail?name=win-sshfs-0.0.1.5-setup.exe) is open-source and installs without hassles up to Windows 7 (and with a few workarounds on Windows 8 as well). It may, however, loose connection after longer periods of inactivity. A commercial alternative (with a free version perfectly sufficient for our purposes) is [SFTP Net Drive](https://www.eldos.com/sftp-net-drive/), which works stable (but does bad things if you disconnect you device without unmounting it first).

On **Mac OSX**, there is a nice tutorial [here](http://fortysomethinggeek.blogspot.de/2012/11/sshfs-on-osx-mount-sshsftp-shares-on-mac.html) that walks you through setting things up with [FUSE for OSX](http://osxfuse.github.io/).

On **Ubuntu**, you can [use Nautilus](http://www.lessons4you.info/how-to-connect-ssh-sftp-and-ftp-servers-using-nautilus-ubuntu-13-04/) or the [command line](http://howto.blbosti.com/2010/09/mount-a-remote-ssh-folder-in-ubuntu-cmd-and-gui/).

With SFTP set up, you now can simply open, edit, create, copy, delete and move files conveniently from your desktop. This can often be more comfortable than doing everything via command line SSH (and SCP).