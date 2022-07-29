# AltLinux
<img src="https://github.com/maxasix/AltLinuxblob/main/resources/4.png" alt="AltLinux Logo"> 

A GUI for AltServer-Linux. It's available for Ubuntu 18.04, Ubuntu 20.04, and Ubuntu 22.04.

Derivatives, such as Linux Mint and Pop!_ OS should also work. If your distribution isn't listed here, you can [run the script without installing](#run-the-script-without-installing). It contains experimental Fedora instructions which may or may not work.

Features:
- A straightforward GUI
- A tray menu that works just like on Windows
- Sideloading AltStore
- Sideloading other apps without AltStore
- While the tray icon is present, AltServer runs in the background in tethered mode
- Launching the tray icon on start-up

The program is in its very early state, so if you're experiencing issues or want to help, you can join [the Discord server](https://discord.gg/vtvxYFAfAR).

## Install AltLinux

Download and install the DEB package [from here](https://github.com/maxasix/AltLinux/releases). 

Read the [Tips And Tricks](#tips-and-tricks) section for more information.

## Uninstall AltLinux

If you want to uninstall AltLinux, run the following commands:

```
sudo apt purge altlinux
```

```
sudo rm -rf /usr/lib/altlinux
```

```
rm -rf $HOME/.local/share/altlinux
```

## Run the script without installing

### Ubuntu:

Add the `universe` repository:

```
sudo add-apt-repository universe -y
```

Install the dependencies:
```
sudo apt-get install binutils python3-pip git gir1.2-appindicator3-0.1 usbmuxd libimobiledevice6 libimobiledevice-utils wget curl libavahi-compat-libdnssd-dev docker.io zlib1g-dev
``` 

Run the following commands:
```
git clone https://github.com/maxasix/AltLinux
```  

```
cd AltLinux
```  

```
python3 main.py
```  

### Fedora:

Install the dependencies:
```
sudo dnf install binutils python3-pip git libappindicator-gtk3 usbmuxd libimobiledevice-devel libimobiledevice-utils wget curl avahi-compat-libdns_sd-devel dnf-plugins-core
```
Add the Docker repo to your Fedora system:
```
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```
Run the following command to install Docker:
```
sudo dnf install docker-ce docker-ce-cli containerd.io
```

Run the following commands:
```
git clone https://github.com/maxasix/AltLinux
```  

```
cd AltLinux
```  

```
python3 main.py
```  

## Compile the package
Add the `universe` repository:

```
sudo add-apt-repository universe -y
```

Install the dependencies:
```
sudo apt-get install binutils python3-pip git gir1.2-appindicator3-0.1 usbmuxd libimobiledevice6 libimobiledevice-utils wget curl libavahi-compat-libdnssd-dev docker.io zlib1g-dev
```  
  
Install pyinstaller:

- Ubuntu 20.04 and later:

```  
pip install pyinstaller
```  

- Ubuntu 18.04 and earlier:

```  
pip3 install pyinstaller
```  

Reboot your computer for changes to take effect.

Proceed by running the following commands:
```
git clone https://github.com/maxasix/AltLinux
```  

```
cd AltLinux
```  

```
./build.sh
```  

The DEB file is ready! You can install it now.

## Tips And Tricks

- AltLinux runs the `alt-anisette-server` Docker package as root by default. This causes a password prompt to appear every time AltLinux is launched on startup. This can be avoided by adding the user to the `docker` group:

```
sudo groupadd docker
```
```
sudo usermod -aG docker $USER
```
Reboot to apply the changes.

- The first startup usually takes from 2 minutes to 2 hours depending on your Internet connection. This is mostly because the `alt-anisette-server` Docker package weighs 2.19 GB. Patience is key.

- AltLinux cannot run with a VPN turned on. Turn off the VPN and restart AltLinux.

## Credits
AltServer-Linux and alt-anisette-server made by [NyaMisty](https://github.com/NyaMisty)

Artwork by [Nebula](https://github.com/itsnebulalol)
