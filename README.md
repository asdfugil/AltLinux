# AltLinux (Formerly AltShell)

This is a GUI for AltServer-Linux. Currently it is designed to work with Ubuntu 22.04 x64.

Features:
- A straightforward GUI
- A tray menu that works just like on Windows
- Sideloading AltStore
- Sideloading other apps without AltStore
- While the tray icon is present, AltServer runs in the background in tethered mode

The program is in its very early state, so any feedback or contributions are welcome.

## READ THIS TO GET STARTED
Install the dependencies:
```
sudo apt-get install binutils python3-pip git gir1.2-appindicator3-0.1 usbmuxd libimobiledevice6 libimobiledevice-utils wget curl libavahi-compat-libdnssd-dev docker.io
```  
  
Install pyinstaller:
```  
pip install pyinstaller
```  

Configure docker to work without sudo:
```
sudo groupadd docker
```
```
sudo usermod -aG docker $USER
```
```
newgrp docker
```

Reboot your computer for changes to take effect.

Now you can download and install [the DEB package](https://github.com/maxasix/AltLinux/releases).
  
If you wish to compile the program instead, run the following commands:

```
git clone https://github.com/maxasix/AltLinux
```  

```
cd AltLinux
```  

```
./build.sh
```  

It takes a long time to get started for the first time. Patience is key.

## Credits
AltServer-Linux and alt-anisette-server made by [NyaMisty](https://github.com/NyaMisty)  
AltServer-LinuxGUI made by [powenn](https://github.com/powenn)
