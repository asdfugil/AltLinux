#!/usr/bin/python
import os
import gi
import requests
import subprocess
import signal
from time import sleep
gi.require_version("Gtk", "3.0")
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator
from gi.repository import GLib
from gi.repository import GdkPixbuf
from gi.repository import Notify
from gi.repository import Gdk 

ermcheck = False
lolcheck = "lol"
AppIcon = ("/usr/lib/altlinux/resources/2.png")
AltServer = ("/usr/lib/altlinux/resources/AltServer")
AltStore = ("/usr/lib/altlinux/resources/AltStore.ipa")
PATH = AltStore
AutoStart = ("/usr/lib/altlinux/resources/LaunchAtLogin.sh")

def connectioncheck():
    timeout = 5
    try:
        requests.get("https://github.com", timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout):
	    return False

# check version
with open(("/usr/lib/altlinux/resources/version"), 'r', encoding='utf-8') as f:
    LocalVersion = f.readline().strip()
LatestVersion=""

def main():
  command1 = 'echo $XDG_CURRENT_DESKTOP | grep -q "GNOME"'
  CheckRun7=subprocess.run(command1,shell=True)
  if CheckRun7.returncode == 1 :
      print("True!")
  elif CheckRun7.returncode == 0 and gtk.StatusIcon.is_embedded :
      print("True!")
  else:
      CheckRun8=subprocess.run(f'python3 /usr/lib/altlinux/resources/oops.py&',shell=True) 
      os.kill(os.getpid(),signal.SIGKILL)
  CheckRun2=subprocess.run(f'python3 /usr/lib/altlinux/resources/wait.py&',shell=True) 
  command = 'curl 127.0.0.1:6969 | grep -q "{"'
  CheckRun=subprocess.run(command,shell=True)
  if CheckRun.returncode == 0 :
      #Running = False
      #os.kill(os.getpid(),signal.SIGKILL)
      print('OK!')
  else :
      CheckRun3=subprocess.run(f'docker pull nyamisty/alt_anisette_server',shell=True) 
      CheckRun4=subprocess.run(f'docker run -d --rm -p 6969:6969 -it nyamisty/alt_anisette_server',shell=True)
      finished = False
      while not finished:
          CheckRun5=subprocess.run(command,shell=True)
          sleep(5)
          if CheckRun5.returncode == 0 :
            finished = True
  CheckRun1=subprocess.run(f'export ALTSERVER_ANISETTE_SERVER="http://127.0.0.1:6969"',shell=True)
  GLib.set_prgname('AltLinux')
  if not os.path.exists(AltStore):
    subprocess.run(f'gksudo curl -L https://cdn.altstore.io/file/altstore/apps/altstore/1_5.ipa > /usr/lib/altlinux/resources/AltStore.ipa',shell=True)
  CheckRun8=subprocess.run(command1,shell=True)
  if CheckRun8.returncode == 0 :
    file_name = "/usr/lib/altlinux/resources/1.png"
  else :
    file_name = "/usr/lib/altlinux/resources/2.png"
  indicator = appindicator.Indicator.new("customtray", os.path.abspath(file_name), appindicator.IndicatorCategory.APPLICATION_STATUS)
  indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
  indicator.set_menu(menu())
  subprocess.run(f'{AltServer} &> /dev/null &',shell=True)
  CheckRun6=subprocess.run(f'pkill -f wait.py',shell=True)
  gtk.main()

def menu():
  menu = gtk.Menu()
  
  if(notify()) == True:
    command_six = gtk.MenuItem('Download Update')
    command_six.connect('activate', showurl)
    menu.append(command_six)
    
    menu.append(gtk.SeparatorMenuItem())

  command_one = gtk.MenuItem('About AltLinux')
  command_one.connect('activate', on_abtdlg)
  menu.append(command_one)
  
  menu.append(gtk.SeparatorMenuItem())

  command_two = gtk.MenuItem('Install AltStore')
  command_two.connect('activate', altstoreinstall)
  menu.append(command_two)
  
  command_three = gtk.MenuItem('Install an IPA file')
  command_three.connect('activate', altserverfile)
  menu.append(command_three)

  command_four = gtk.MenuItem('Pair')
  command_four.connect('activate', lol)
  menu.append(command_four)

  command_five = gtk.MenuItem('Restart AltServer')
  command_five.connect('activate', lol123)
  menu.append(command_five)
  
  menu.append(gtk.SeparatorMenuItem())
  
  #command_six = gtk.CheckMenuItem('Launch at Login')
  #command_six.set_active(command_six)
  #command_six.connect('activate', showurl)
  #menu.append(command_six)


  exittray = gtk.MenuItem('Quit AltLinux')
  exittray.connect('activate', quit)
  menu.append(exittray)
  
  menu.show_all()
  return menu
  
def note(_):
  os.system("gedit $HOME/Documents/notes.txt")

def on_abtdlg(self):
  about = gtk.AboutDialog()
  width = 50
  height = 50
  pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('/usr/lib/altlinux/resources/2.png', width, height)
  about.set_logo(pixbuf)
  about.set_program_name("AltLinux")
  about.set_version("0.3.7")
  about.set_authors(['maxasix', 'AltServer-Linux and alt-anisette-server', 'made by NyaMisty on Github', 'AltServer-LinuxGUI', 'made by powenn on Github'])
  about.set_comments("A GUI for AltServer-Linux written in Python and PyGObject.")
  about.set_website("https://github.com/maxasix/AltLinux")
  about.set_copyright("GUI by maxasix")
  about.set_position(gtk.WindowPosition.CENTER)
  about.run()
  about.destroy()

def paircheck():
  pairchecking=subprocess.run('idevicepair pair | grep -q "SUCCESS"',shell=True)
  if pairchecking.returncode == 0 :
    return False
  else :
    return True

def altstoreinstall(_):
  if paircheck():
    global lolcheck
    lolcheck = "altstr"
    lol(_)
  else:
    win1()
def altserverfile(_):
  if paircheck():
    global lolcheck
    lolcheck = "ipa"
    lol(_)
  else:
    on_file()
    global ermcheck
    if ermcheck == True:
      global PATH
      PATH = FileChooserWindow().PATHFILE
    win1()
    ermcheck == False


class login(gtk.Window):
   def __init__(self):
        super().__init__(title="Login")
        self.present()
        self.set_position(gtk.WindowPosition.CENTER)
        self.set_resizable( False )
        #self.set_size_request(200, 100)
        self.set_border_width(10)
        
        grid = gtk.Grid()
        self.add(grid)
        
        #self.set_border_height(20)
        #self.timeout_id = None
        label = gtk.Label(label="Apple ID: ")
        label.set_justify(gtk.Justification.LEFT)
        
        self.entry1 = gtk.Entry()

        label1 = gtk.Label(label="Password: ")
        label1.set_justify(gtk.Justification.LEFT)

        self.entry = gtk.Entry()
        self.entry.set_visibility(False)

        #self.check_editable = gtk.CheckButton(label="Editable")
        #self.check_editable.connect("toggled", self.on_editable_toggled)
        #self.check_editable.set_active(True)
        #hbox.pack_start(self.check_editable, True, True, 0)

        #self.check_visible = gtk.CheckButton(label="Visible")
        #self.check_visible.connect("toggled", self.on_visible_toggled)
        #self.check_visible.set_active(True)
        #hbox.pack_start(self.check_visible, True, True, 0)

        #self.pulse = gtk.CheckButton(label="Pulse")
        #self.pulse.connect("toggled", self.on_pulse_toggled)
        #self.pulse.set_active(False)
        #hbox.pack_start(self.pulse, True, True, 0)

        #self.icon = gtk.CheckButton(label="Icon")
        #self.icon.connect("toggled", self.on_icon_toggled)
        #self.icon.set_active(False)
        #hbox.pack_start(self.icon, True, True, 0)
        
        #image = gtk.Image()
        #image.show()
        #image.set_from_file(os.path.join("2.png"))
        #hbox.pack_start(image, True, True, 0)
        
        button = gtk.Button.new_with_label("Login")
        button.connect("clicked", self.on_click_me_clicked)
        
        grid.add(label)
        grid.attach(self.entry1, 1, 0, 2, 1)
        grid.attach_next_to(label1, label, gtk.PositionType.BOTTOM, 1, 2)
        grid.attach(self.entry, 1, 2, 1, 1)
        grid.attach_next_to(button, self.entry, gtk.PositionType.RIGHT, 1, 1)
          
   def on_click_me_clicked(self, button):
        print('"Click me" button was clicked')
        self.entry.set_progress_pulse_step(0.2)
        # Call self.do_pulse every 100 ms
        self.timeout_id = GLib.timeout_add(100, self.do_pulse, None)
        self.entry.set_editable(False)
        self.entry1.set_editable(False)
        button.set_sensitive(False)
        AppleID = self.entry1.get_text().lower()
        Password = self.entry.get_text()
        print(AppleID)
        print(Password)
        #DeviceCheck=subprocess.run('idevicepair pair',shell=True)
        #if DeviceCheck.returncode == 1 :
        #  try:
        #    lol()
        #  except:
        #    print('Error!')
        #if DeviceCheck.returncode == 0 :
        print('resource path check!')
        _udid = subprocess.check_output("lsusb -v 2> /dev/null | grep -e 'Apple Inc' -A 2 | grep iSerial | awk '{print $3}'",shell=True).decode().strip()
        print('first udid command check!')
        _udid_length = len(_udid)
        print('second udid command check!')
        if _udid_length == 24 :
          UDID = _udid[:8] + '-' + _udid[8:]
          print('third(1) udid command check!')
        elif _udid_length == 40 :
          UDID = _udid
          print('third(2) udid command check!')
        InsAltStoreCMD=f'{("/usr/lib/altlinux/resources/AltServer")} -u {UDID} -a {AppleID} -p {Password} {PATH} > {("log.txt")}'
        print('insaltstorecmd declared!')
        InsAltStore=subprocess.Popen(InsAltStoreCMD, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        print('insaltstorecmd ran!')
        Installing = True
        print('installing true!')
        WarnTime=0
        print('warntime 0!')
        while Installing :  
          CheckIns=subprocess.run(f'grep "Press any key to continue..." {("log.txt")}',shell=True)
          #CheckWarn=subprocess.run(f'grep "Are you sure you want to continue?" {("log.txt")}',shell=True)
          CheckSuccess=subprocess.run(f'grep "Installation Succeeded" {("log.txt")}',shell=True)
          Check2fa=subprocess.run(f'grep "Enter two factor code" {("log.txt")}',shell=True)
          if CheckIns.returncode == 0 :
              Installing = False
              InsAltStore.terminate()
              print('Fail!')
              self.fail()
              self.destroy()  
          if Check2fa.returncode == 0 and WarnTime == 0 :
              Installing = False
              print("Requires two factor! Awooga!")
              Warnmsg=subprocess.check_output(f"tail -8 {('log.txt')}",shell=True).decode()
              Installing = False
              dialog = DialogExample(self)
              response = dialog.run()
              if response == gtk.ResponseType.OK:
                vercode = dialog.entry2.get_text()
                vercode = vercode+"\n"
                vercodebytes = bytes(vercode.encode())
                print(vercodebytes)
                Installing = True
                InsAltStore.communicate(input=vercodebytes)
                dialog.destroy()
                WarnTime = 1
                #self.destroy()
              elif response == gtk.ResponseType.CANCEL:
                Installing = False
                print('Fail!')
                self.fail()
                self.destroy()
          if CheckSuccess.returncode == 0 :
              Installing = False
              print('Success!')
              self.success()
              self.destroy() 
   def success(self):
      self.set_position(gtk.WindowPosition.CENTER)
      dialog = gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=gtk.MessageType.INFO,
            buttons=gtk.ButtonsType.OK,
            text="Success!",
      )
      dialog.format_secondary_text(
            "Operation completed."
      )
      dialog.run()
      print("INFO dialog closed")

      dialog.destroy()

   def fail(self):
       self.set_position(gtk.WindowPosition.CENTER)
       dialog = gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=gtk.MessageType.ERROR,
            buttons=gtk.ButtonsType.OK,
            text="Fail!",
      )
       dialog.format_secondary_text(
            "Operation failed."
      )
       dialog.run()
       print("ERROR dialog closed")

       dialog.destroy()


   def on_editable_toggled(self, button):
        value = button.get_active()
        self.entry.set_editable(value)

   def on_pulse_toggled(self, button):
       if button.get_active():
            self.entry.set_progress_pulse_step(0.2)
            # Call self.do_pulse every 100 ms
            self.timeout_id = GLib.timeout_add(100, self.do_pulse, None)
       else:
            # Don't call self.do_pulse anymore
            GLib.source_remove(self.timeout_id)
            self.timeout_id = None
            self.entry.set_progress_pulse_step(0)

   def do_pulse(self, user_data):
        self.entry.progress_pulse()
        return True
   #def on_icon_toggled(self, button):
   #    if button.get_active():
   #         icon_name = "system-lock-screen-symbolic"
   #    else:
   #         icon_name = None
   #    self.entry.set_icon_from_icon_name(gtk.EntryIconPosition.PRIMARY, icon_name)

class testing(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self, title="Pair your device")
        self.present()
        self.set_position(gtk.WindowPosition.CENTER)
        self.set_resizable( False )
        #self.set_border_width(10)
        self.set_border_width(20)
        #self.set_default_size(150, 100)
        hbox = gtk.Box(orientation=gtk.Orientation.VERTICAL)
        
        lbl1 = gtk.Label("Please make sure your device is connected to the computer.\nPress 'Pair' to pair your device.")
        #lbl1.set_property("margin_left", 40)
        #lbl1.set_property("margin_right", 40)
        hbox.pack_start(lbl1, False, False, 0)

        button = gtk.Button(label="Pair")
        button.connect("clicked", self.on_info_clicked)
        hbox.pack_start(button, False, False, 10)

        self.add(button)
        self.add(hbox)

    def on_info_clicked(self, widget):
        try:
          subprocess.run(['idevicepair pair'], shell=True, check=True)
        except subprocess.CalledProcessError as e:
          print (e.output)
        dialog = gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=gtk.MessageType.INFO,
            buttons=gtk.ButtonsType.OK,
            text="Accept the trust dialog on the screen of your device,\nthen press 'OK'.",
        )
        #dialog.format_secondary_text(
        #    "And this is the secondary text that explains things."
        #)
        dialog.run()
        print("INFO dialog closed")
        try:
          subprocess.run(['idevicepair pair'], shell=True, check=True, capture_output=True)
          self.destroy()
          global lolcheck
          if lolcheck == "altstr":
            win1()
          elif lolcheck == "ipa":
            on_file()
          global ermcheck
          if ermcheck == True:
            global PATH
            PATH = FileChooserWindow().PATHFILE
            win1()
            ermcheck == False
          elif lolcheck == "lol":
            print('OK!!')
          lolcheck = "lol"
        except subprocess.CalledProcessError as e:
          #print (e.output)
          errmoment = e.output
          dialog1 = gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=gtk.MessageType.ERROR,
            buttons=gtk.ButtonsType.OK,
            #text=e.output,
            text=(errmoment[:-2]),
            #text.select_region(0,-1),
            )
          dialog1.run()
          dialog1.destroy()
        dialog.destroy()
        

class FileChooserWindow(gtk.Window):
    def __init__(self):
        super().__init__(title="FileChooser Example")
        box = gtk.Box(spacing=6)
        self.add(box)

        dialog = gtk.FileChooserDialog(
            title="Please choose a file", parent=self, action=gtk.FileChooserAction.OPEN
        )
        dialog.add_buttons(
            gtk.STOCK_CANCEL,
            gtk.ResponseType.CANCEL,
            gtk.STOCK_OPEN,
            gtk.ResponseType.OK,
        )

        self.add_filters(dialog)

        response = dialog.run()
        if response == gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
            self.PATHFILE = dialog.get_filename()
            global ermcheck
            ermcheck = True
        elif response == gtk.ResponseType.CANCEL:
            print("Cancel clicked")
            self.destroy()

        dialog.destroy()
        #win4 = login()
        #win4.show_all()

    def add_filters(self, dialog):
        filter_ipa = gtk.FileFilter()
        filter_ipa.set_name("IPA files")
        filter_ipa.add_pattern("*.ipa")
        dialog.add_filter(filter_ipa)

        filter_any = gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

class DialogExample(gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title="Verification code", transient_for=parent, flags=0)
        self.present()
        self.add_buttons(
            gtk.STOCK_CANCEL, gtk.ResponseType.CANCEL, gtk.STOCK_OK, gtk.ResponseType.OK
        )
        self.set_resizable( False )
        #self.set_size_request(200, 100)
        self.set_border_width(10)

        labelhelp = gtk.Label(label="Enter the verification \ncode on your device: ")
        labelhelp.set_justify(gtk.Justification.CENTER)

        self.entry2 = gtk.Entry()

        box = self.get_content_area()
        box.add(labelhelp)
        box.add(self.entry2)
        self.show_all()

def notify():
  if(connectioncheck()) == True:
    LatestVersion=subprocess.check_output("curl -Lsk https://github.com/maxasix/AltLinux/raw/main/version",shell=True).decode()
    if LatestVersion > LocalVersion :
      Notify.init("MyProgram")
      command2 = 'echo $XDG_CURRENT_DESKTOP | grep -q "GNOME"'
      CheckRun9=subprocess.run(command2,shell=True)
      if CheckRun9.returncode == 0 :
        file_name1 = "/usr/lib/altlinux/resources/1.png"
      else :
        file_name1 = "/usr/lib/altlinux/resources/2.png"
      n = Notify.Notification.new("An update is available!","Click 'Download Update' in the tray menu.", os.path.abspath(file_name1))
      n.set_timeout(Notify.EXPIRES_DEFAULT)
      #n.add_action("newupd", "Download", actionCallback)
      n.show()  
      return True
    else:
      return False
  else:
      return False

def showurl(_):
  gtk.show_uri_on_window(None, "https://github.com/maxasix/AltLinux/releases", Gdk.CURRENT_TIME)
  subprocess.run(f'killall {AltServer}',shell=True)
  gtk.main_quit()
  os.kill(os.getpid(),signal.SIGKILL)

def on_file():
  win2 = FileChooserWindow()

def lol(_):
  window = testing() 
  window.show_all()

def lol123(_):
    subprocess.run(f'killall {AltServer}',shell=True)
    subprocess.run('idevicepair pair',shell=True)
    subprocess.run(f'{AltServer} &> /dev/null &',shell=True)

def win1():
  win3 = login()
  win3.show_all()

def win2(_):
  win4 = login()
  win4.show_all()

def actionCallback(notification, action, user_data = None):
    gtk.show_uri_on_window(None, "https://github.com/maxasix/AltLinux/releases", Gdk.CURRENT_TIME)
    subprocess.run(f'killall {AltServer}',shell=True)
    gtk.main_quit()
    os.kill(os.getpid(),signal.SIGKILL)

def quit(_):
  subprocess.run(f'killall {AltServer}',shell=True)
  gtk.main_quit()
  os.kill(os.getpid(),signal.SIGKILL)
  
if __name__ == "__main__":
  main()
