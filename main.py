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

installedcheck = False
def resource_path(relative_path):
    global installedcheck
    CheckRun10=subprocess.run(f'find /usr/lib/altlinux/altlinux 2>/dev/null >dev/null',shell=True)
    if CheckRun10.returncode == 0 :
      installedcheck = True
      base_path = '/usr/lib/altlinux/altlinux'
    else :
      base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
ermcheck = False
lolcheck = "lol"
Warnmsg = "warn"
command_six = gtk.CheckMenuItem('Launch at Login')
AppIcon = resource_path("resources/2.png")
AltServer = resource_path("resources/AltServer")
AltStore = resource_path("resources/AltStore.ipa")
PATH = AltStore
AutoStart = resource_path("resources/AutoStart.sh")

def connectioncheck():
    timeout = 5
    try:
        requests.get("https://github.com", timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout):
	    return False

# check version
with open(resource_path("resources/version"), 'r', encoding='utf-8') as f:
    LocalVersion = f.readline().strip()
LatestVersion=""

def main():
  CheckRun12=subprocess.run(f'mkdir /home/$(whoami)/.altlinux',shell=True)
  global installedcheck
  command1 = 'echo $XDG_CURRENT_DESKTOP | grep -q "GNOME"'
  CheckRun7=subprocess.run(command1,shell=True)
  if CheckRun7.returncode == 1 :
      print("True!")
  elif CheckRun7.returncode == 0 and gtk.StatusIcon.is_embedded :
      print("True!")
  else:
      if installedcheck :
        CheckRun8=subprocess.run(f'python3 /usr/lib/altlinux/resources/oops.py&',shell=True) 
      else :
        CheckRun8=subprocess.run(f'python3 ./resources/oops.py&',shell=True) 
      os.kill(os.getpid(),signal.SIGKILL)
  if installedcheck :
        CheckRun8=subprocess.run(f'python3 /usr/lib/altlinux/resources/wait.py&',shell=True) 
  else :
        CheckRun8=subprocess.run(f'python3 ./resources/wait.py&',shell=True) 
  command = 'curl 127.0.0.1:6969 | grep -q "{"'
  CheckRun=subprocess.run(command,shell=True)
  if CheckRun.returncode == 0 :
      #Running = False
      #os.kill(os.getpid(),signal.SIGKILL)
      print('OK!')
  else :
    CheckRunA=subprocess.run('id -nG "$USER" | grep -qw docker',shell=True)
    if CheckRunA.returncode == 0 :
      CheckRun3=subprocess.run(f'pkexec sh -c "docker pull nyamisty/alt_anisette_server && docker run -d --rm -p 6969:6969 -it nyamisty/alt_anisette_server"',shell=True) 
    else :
      CheckRun3=subprocess.run(f'docker pull nyamisty/alt_anisette_server && docker run -d --rm -p 6969:6969 -it nyamisty/alt_anisette_server',shell=True) 
    finished = False
    while not finished:
          CheckRun5=subprocess.run(command,shell=True)
          sleep(3)
          if CheckRun5.returncode == 0 :
            finished = True
  GLib.set_prgname('AltLinux')
  if not os.path.exists(AltStore):
    if installedcheck :
      subprocess.run(f'pkexec curl -L https://cdn.altstore.io/file/altstore/apps/altstore/1_5.ipa > /usr/lib/altlinux/resources/AltStore.ipa',shell=True)
    else :
      subprocess.run(f'curl -L https://cdn.altstore.io/file/altstore/apps/altstore/1_5.ipa > ./resources/AltStore.ipa',shell=True)
  CheckRun8=subprocess.run(command1,shell=True)
  if CheckRun8.returncode == 0 :
    file_name = resource_path("resources/1.png")
  else :
    file_name = resource_path("resources/2.png")
  indicator = appindicator.Indicator.new("customtray", os.path.abspath(file_name), appindicator.IndicatorCategory.APPLICATION_STATUS)
  indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
  indicator.set_menu(menu())
  subprocess.run(f'export ALTSERVER_ANISETTE_SERVER="http://127.0.0.1:6969" & {AltServer} &> /dev/null &',shell=True)
  CheckRun6=subprocess.run(f'pkill -f wait.py',shell=True)
  gtk.main()

def menu():
  menu = gtk.Menu()
  
  if(notify()) == True:
    command_upd = gtk.MenuItem('Download Update')
    command_upd.connect('activate', showurl)
    menu.append(command_upd)
    
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
  
  CheckRun11=subprocess.run(f'test -e /usr/lib/altlinux/altlinux',shell=True)
  if CheckRun11.returncode == 0 :
    global command_six
    CheckRun12=subprocess.run(f'test -e /home/$(whoami)/.config/autostart/AltLinux.desktop',shell=True)
    if CheckRun12.returncode == 0 :
      command_six.set_active(command_six)
    command_six.connect('activate', launchatlogin1)
    menu.append(command_six)
  
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
  pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(resource_path('resources/2.png'), width, height)
  about.set_logo(pixbuf)
  about.set_program_name("AltLinux")
  about.set_version("0.3.8")
  about.set_authors(['maxasix', 'AltServer-Linux and alt-anisette-server', 'made by NyaMisty on Github', 'AltServer-LinuxGUI', 'made by powenn on Github'])
  about.set_comments("A GUI for AltServer-Linux written in Python and PyGObject.")
  about.set_website("https://github.com/maxasix/AltLinux")
  about.set_copyright("GUI by maxasix")
  about.set_position(gtk.WindowPosition.CENTER_ALWAYS)
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
        self.set_position(gtk.WindowPosition.CENTER_ALWAYS)
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
        _udid = subprocess.check_output("lsusb -v 2> /dev/null | grep -e 'Apple Inc' -A 2 | grep iSerial | awk '{print $3}'",shell=True).decode().strip()
        _udid_length = len(_udid)
        if _udid_length == 24 :
          UDID = _udid[:8] + '-' + _udid[8:]
        elif _udid_length == 40 :
          UDID = _udid
        global installedcheck
        if installedcheck :
          InsAltStoreCMD=f'''{("export ALTSERVER_ANISETTE_SERVER='http://127.0.0.1:6969' && cp /usr/lib/altlinux/resources/AltServer /home/$(whoami)/.altlinux/AltServer && /home/$(whoami)/.altlinux/AltServer")} -u {UDID} -a {AppleID} -p {Password} {PATH} > {("/home/$(whoami)/.altlinux/log.txt")}'''
        else :
          InsAltStoreCMD=f'''{("export ALTSERVER_ANISETTE_SERVER='http://127.0.0.1:6969' && ./resources/AltServer")} -u {UDID} -a {AppleID} -p {Password} {PATH} > {("/home/$(whoami)/.altlinux/log.txt")}'''
        InsAltStore=subprocess.Popen(InsAltStoreCMD, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        Installing = True
        WarnTime=0
        while Installing :  
          CheckIns=subprocess.run(f'grep "Press any key to continue..." {("/home/$(whoami)/.altlinux/log.txt")}',shell=True)
          CheckWarn=subprocess.run(f'grep "Are you sure you want to continue?" {("/home/$(whoami)/.altlinux/log.txt")}',shell=True)
          CheckSuccess=subprocess.run(f'grep "Notify: Installation Succeeded" {("/home/$(whoami)/.altlinux/log.txt")}',shell=True)
          Check2fa=subprocess.run(f'grep "Enter two factor code" {("/home/$(whoami)/.altlinux/log.txt")}',shell=True)
          if CheckIns.returncode == 0 and WarnTime == 1:
              Installing = False
              InsAltStore.terminate()
              print('Fail!')
              self.fail()
              subprocess.run(f'rm /home/$(whoami)/.altlinux/AltServer',shell=True)
              subprocess.run(f'rm /home/$(whoami)/.altlinux/AltServer/AltServerData',shell=True)
              self.destroy()  
              WarnTime == 1
          if CheckWarn.returncode == 0 and WarnTime == 0 :
                    Installing = False
                    global Warnmsg
                    Warnmsg=subprocess.check_output(f"tail -8 {('/home/$(whoami)/.altlinux/log.txt')}",shell=True).decode()
                    dialog = DialogExample2(self)
                    response = dialog.run()
                    if response == gtk.ResponseType.OK:
                      dialog.destroy()
                      InsAltStore.communicate(input=b'\n')
                      WarnTime = 1
                      Installing = True
                    elif response == gtk.ResponseType.CANCEL:
                      dialog.destroy()
                      self.cancel()
                      WarnTime = 1

          if Check2fa.returncode == 0 and WarnTime == 0 :
              print("Requires two factor! Awooga!")
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
                print('Fail!')
                self.cancel()
                WarnTime = 1
                subprocess.run(f'rm /home/$(whoami)/.altlinux/AltServer',shell=True)
                subprocess.run(f'rm /home/$(whoami)/.altlinux/AltServer/AltServerData',shell=True)
                self.destroy()
          if CheckSuccess.returncode == 0 :
              Installing = False
              print('Success!')
              self.success()
              subprocess.run(f'rm /home/$(whoami)/.altlinux/AltServer',shell=True)
              subprocess.run(f'rm /home/$(whoami)/.altlinux/AltServer/AltServerData',shell=True)
              self.destroy() 
   def success(self):
      self.set_position(gtk.WindowPosition.CENTER_ALWAYS)
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

   def cancel(self):
      self.set_position(gtk.WindowPosition.CENTER_ALWAYS)
      dialog = gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=gtk.MessageType.INFO,
            buttons=gtk.ButtonsType.OK,
            text="Cancelled",
      )
      dialog.format_secondary_text(
            "Operation cancelled by user"
      )
      dialog.run()
      print("INFO dialog closed")

      dialog.destroy()

   def fail(self):
       self.set_position(gtk.WindowPosition.CENTER_ALWAYS)
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
        self.set_position(gtk.WindowPosition.CENTER_ALWAYS)
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

class DialogExample2(gtk.Dialog):
    def __init__(self, parent):
        global Warnmsg
        super().__init__(title="Warning", transient_for=parent, flags=0)
        self.present()
        self.add_buttons(
            gtk.STOCK_CANCEL, gtk.ResponseType.CANCEL, gtk.STOCK_OK, gtk.ResponseType.OK
        )
        self.set_resizable( False )
        #self.set_size_request(200, 100)
        self.set_border_width(10)

        labelhelp = gtk.Label(label="Are you sure you want to continue?")
        labelhelp.set_justify(gtk.Justification.CENTER)

        labelhelp1 = gtk.Label(label=Warnmsg)
        labelhelp1.set_justify(gtk.Justification.CENTER)
        labelhelp1.set_line_wrap(True)
        labelhelp1.set_max_width_chars(48)
        labelhelp1.set_selectable(True)

        box = self.get_content_area()
        box.add(labelhelp)
        box.add(labelhelp1)
        self.show_all()

def notify():
  if(connectioncheck()) == True:
    LatestVersion=subprocess.check_output("curl -Lsk https://github.com/maxasix/AltLinux/raw/main/version",shell=True).decode()
    if LatestVersion > LocalVersion :
      Notify.init("MyProgram")
      command2 = 'echo $XDG_CURRENT_DESKTOP | grep -q "GNOME"'
      CheckRun9=subprocess.run(command2,shell=True)
      if CheckRun9.returncode == 0 :
        file_name1 = resource_path("resources/1.png")
      else :
        file_name1 = resource_path("resources/2.png")
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

def launchatlogin1(_):
    global command_six
    if command_six.get_active():
      global AutoStart
      os.popen(AutoStart).read()
      return True
    else :
    #if file_exists :
      subprocess.run(f'rm /home/$(whoami)/.config/autostart/AltLinux.desktop',shell=True)
      return False

def quit(_):
  subprocess.run(f'killall {AltServer}',shell=True)
  gtk.main_quit()
  os.kill(os.getpid(),signal.SIGKILL)
  
if __name__ == "__main__":
  main()
