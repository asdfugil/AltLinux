# AltLinux

This is a GUI for AltServer-Linux. Currently it is designed to work with Ubuntu 22.04 x64.

Features:
- A straightforward GUI
- A tray menu that works just like on Windows
- Sideloading AltStore
- Sideloading other apps without AltStore
- While the tray icon is present, AltServer runs in the background in tethered mode
- Launching the tray icon on start-up

The program is in its very early state, so any feedback or contributions are welcome.

## Install AltLinux

Download and install the DEB package [from here](https://github.com/maxasix/AltLinux/releases). 

You can read the [Tips And Tricks](#tips-and-tricks) section for additional information.

## Run the script without installing
Install the dependencies:
```
sudo apt-get install binutils python3-pip git gir1.2-appindicator3-0.1 usbmuxd libimobiledevice6 libimobiledevice-utils wget curl libavahi-compat-libdnssd-dev docker.io
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
Install the dependencies:
```
sudo apt-get install binutils python3-pip git gir1.2-appindicator3-0.1 usbmuxd libimobiledevice6 libimobiledevice-utils wget curl libavahi-compat-libdnssd-dev docker.io
```  
  
Install pyinstaller:
```  
pip install pyinstaller
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

- Due to the fact that the `alt-anisette-server` Docker package is quite heavy in its size, it takes a long time to get started for the first time. Patience is key.

- AltLinux runs the `alt-anisette-server` Docker package as root by default. This causes a password prompt to appear every time AltLinux is launched on startup. This can be avoided by adding the user to the `docker` group:
```
sudo groupadd docker
```
```
sudo usermod -aG docker $USER
```
Reboot to apply the changes.

## Credits
AltServer-Linux and alt-anisette-server made by [NyaMisty](https://github.com/NyaMisty)  
AltServer-LinuxGUI made by [powenn](https://github.com/powenn)
