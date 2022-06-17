# AltShell (Originally AltServer-Linux-ShellScript)

This is merely a fork to see if I can get the program running on Ubuntu 22.04 x64.

## Get started
Run the following command in your terminal to install the dependencies:
```
sudo apt-get install usbmuxd libimobiledevice6 libimobiledevice-utils wget curl libavahi-compat-libdnssd-dev docker.io
```  
  
Before running the script, run the following commands:  
```
docker pull nyamisty/alt_anisette_server
```  
```  
docker run -d --rm -p 6969:6969 -it nyamisty/alt_anisette_server
```  
```  
curl 127.0.0.1:6969
```  
If the last command shows output that starts with `{"X-Apple-I-Client-Time":`, continue. If it doesn't, wait for a few seconds and try again.  
```  
export ALTSERVER_ANISETTE_SERVER="http://127.0.0.1:6969"
```  
  
Run the following command to start the script:
```
./run.sh
```  

## Newbie's corner
Once the script is started, type "p" to pair your device.  
Accept the trust dialog on the screen of your device, then type "p" again.  
Then type "i". Choose option 1 if you want to install AltStore.  
IMPORTANT: type your e-mail in **lowercase** letters, otherwise it might not work.  
  
## Credits
AltServer-Linux and alt-anisette-server made by [NyaMisty](https://github.com/NyaMisty)  
Original script made by [powenn](https://github.com/powenn)