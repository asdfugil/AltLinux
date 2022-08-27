# AltLinux
<img src="https://github.com/maxasix/AltLinux/blob/main/resources/4.png" alt="AltLinux Logo"> 

AltLinux is a GUI for AltServer-Linux that allows to easily sideload apps onto an iPhone, an iPad, or an iPod Touch. It supports iOS 12.2 and later.

Features:
- A straightforward GUI
- A tray menu that works just like on Windows
- Sideloading AltStore
- Sideloading other apps without AltStore
- While the tray icon is present, AltServer runs in the background in tethered mode
- Launching the tray icon on start-up

The program is in its very early state, so if you're experiencing issues or want to help, you can join [the Discord server](https://discord.gg/vtvxYFAfAR).

## Install AltLinux

AltLinux is available for Ubuntu 22.04, Ubuntu 20.04, and Ubuntu 18.04. Only x86_64 architecture is supported at the moment.

Derivatives, such as Linux Mint and Pop!_ OS should also work. To make sure which DEB package to pick, run the following command:

```
python3 --version
```

| Python 3.10          | Python 3.8        |
|:--------------------:|:-----------------:|
| Ubuntu 22.04         | Ubuntu 20.04      |
| Pop!_OS 22.04        | Pop!_OS 20.04     |
| Linux Mint 21        | Linux Mint 20     |
| elementary OS 7      | elementary OS 6   |
| Zorin OS 17          | Zorin OS 16       |

Download and install the DEB package [from here](https://github.com/maxasix/AltLinux/releases). 

If you're running Ubuntu 20.04 or any distro based on it (such as Mint 20), run the following commands:
```
sudo add-apt-repository ppa:apandada1/libhandy-1
sudo apt update
sudo apt install libhandy-1-0 libhandy-1-dev
```

Then install the DEB package [from here](https://github.com/maxasix/AltLinux/releases).

If your distribution isn't based on Ubuntu, you can [run the script without installing](#run-the-script-without-installing). It contains experimental Fedora and Arch Linux instructions which may or may not work.

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
sudo apt-get install binutils python3-pip git gir1.2-appindicator3-0.1 usbmuxd libimobiledevice6 libimobiledevice-utils wget curl libavahi-compat-libdnssd-dev zlib1g-dev unzip usbutils
``` 

IF YOU'RE RUNNING UBUNTU 20.04 OR ITS [DERIVATIVES](https://github.com/maxasix/AltLinux#install-altlinux):
```
sudo add-apt-repository ppa:apandada1/libhandy-1
sudo apt update
sudo apt install libhandy-1-0 libhandy-1-dev
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
sudo dnf install binutils python3-pip git libappindicator-gtk3 usbmuxd libimobiledevice-devel libimobiledevice-utils wget curl avahi-compat-libdns_sd-devel dnf-plugins-core unzip usbutils
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

### Arch Linux

Install the dependencies:
```
sudo pacman -S binutils wget curl git python-pip libappindicator-gtk3 usbmuxd libimobiledevice avahi zlib unzip usbutils
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

## Compile the DEB package
Add the `universe` repository:

```
sudo add-apt-repository universe -y
```

Install the dependencies:
```
sudo apt-get install binutils python3-pip git gir1.2-appindicator3-0.1 usbmuxd libimobiledevice6 libimobiledevice-utils wget curl libavahi-compat-libdnssd-dev zlib1g-dev unzip usbutils
```  

If you're running Ubuntu 20.04 or any distro based on it (such as Mint 20), run the following commands:
```
sudo add-apt-repository ppa:apandada1/libhandy-1
sudo apt update
sudo apt install libhandy-1-0 libhandy-1-dev
```
  
Install pyinstaller:

```  
pip3 install pyinstaller
```  

Reboot your computer for changes to take effect.

After that, proceed by running the following commands:
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

## Credits
AltServer-Linux made by [NyaMisty](https://github.com/NyaMisty)

Artwork by [Nebula](https://github.com/itsnebulalol)

Provision by [Dadoum](https://github.com/Dadoum)
