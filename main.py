#!/usr/bin/python
import os
from re import T
import gi
import requests
import subprocess
import signal
import threading
from threading import Thread
from time import sleep
gi.require_version("Gtk", "3.0")
gi.require_version("Handy", "1")
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')
from gi.repository import Gtk, AppIndicator3 as appindicator
from gi.repository import GLib
from gi.repository import GObject, Handy
from gi.repository import GdkPixbuf
from gi.repository import Notify
from gi.repository import Gdk 
GObject.type_ensure(Handy.ActionRow)

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
splcheck = False
lolcheck = "lol"
Warnmsg = "warn"
nprogress = 0.5
icon_name = "view-conceal-symbolic.symbolic"
command_six = Gtk.CheckMenuItem('Launch at Login')
AppIcon = resource_path("resources/2.png")
AltServer = "/home/$(whoami)/.altlinux/AltServer"
AltStore = "/home/$(whoami)/.altlinux/AltStore.ipa"
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
  GLib.set_prgname('AltLinux')
  subprocess.run(f'mkdir /home/$(whoami)/.altlinux',shell=True)
  global installedcheck
  command1 = 'echo $XDG_CURRENT_DESKTOP | grep -q "GNOME"'
  CheckRun8=subprocess.run(command1,shell=True)
  if CheckRun8.returncode == 0 :
    file_name = resource_path("resources/1.png")
  else :
    file_name = resource_path("resources/2.png")
  CheckRun7=subprocess.run(command1,shell=True)
  if CheckRun7.returncode == 1 or (CheckRun7.returncode == 0 and Gtk.StatusIcon.is_embedded) :
    print("True!")
    if connectioncheck() :
      #splScr = SplashScreen()
      #splScr.show_all()
      indicator = appindicator.Indicator.new("customtray", os.path.abspath(file_name), appindicator.IndicatorCategory.APPLICATION_STATUS)
      indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
      indicator.set_menu(menu())
    else :
      loloopsint()
  else:
    loloops()
  #lol321()
  #rthread = threading.Thread(target=splashcheck)
  #rthread.start()
  Handy.init()
  Gtk.main()

def menu():
  #splash = SplashScreen()
  #splash.start()
  #rthread = threading.Thread(target=splashcheck)
  #rthread.start()
  #global splcheck
  #checked = False
  #while not checked:
  #  if splcheck:
  #    SplashScreen().destroy()
  #  else:
  #    sleep(3)
  menu = Gtk.Menu()
  
  if(notify()) == True:
    command_upd = Gtk.MenuItem('Download Update')
    command_upd.connect('activate', showurl)
    menu.append(command_upd)
    
    menu.append(Gtk.SeparatorMenuItem())

  command_one = Gtk.MenuItem('About AltLinux')
  command_one.connect('activate', on_abtdlg)
  menu.append(command_one)
  
  menu.append(Gtk.SeparatorMenuItem())

  command_two = Gtk.MenuItem('Install AltStore')
  command_two.connect('activate', altstoreinstall)
  menu.append(command_two)
  
  command_three = Gtk.MenuItem('Install an IPA file')
  command_three.connect('activate', altserverfile)
  menu.append(command_three)

  command_four = Gtk.MenuItem('Pair')
  command_four.connect('activate', lol)
  menu.append(command_four)

  command_five = Gtk.MenuItem('Restart AltServer')
  command_five.connect('activate', lol123)
  menu.append(command_five)
  
  menu.append(Gtk.SeparatorMenuItem())
  
  CheckRun11=subprocess.run(f'test -e /usr/lib/altlinux/altlinux',shell=True)
  if CheckRun11.returncode == 0 :
    global command_six
    CheckRun12=subprocess.run(f'test -e /home/$(whoami)/.config/autostart/AltLinux.desktop',shell=True)
    if CheckRun12.returncode == 0 :
      command_six.set_active(command_six)
    command_six.connect('activate', launchatlogin1)
    menu.append(command_six)
  
  exittray = Gtk.MenuItem('Quit AltLinux')
  exittray.connect('activate', quit)
  menu.append(exittray)
  
  menu.show_all()
  lol321()
  return menu
  
def note(_):
  os.system("gedit $HOME/Documents/notes.txt")

def on_abtdlg(self):
  about = Gtk.AboutDialog()
  width = 100
  height = 100
  pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(resource_path('resources/3.png'), width, height)
  about.set_logo(pixbuf)
  about.set_program_name("AltLinux")
  about.set_version("0.4.1")
  about.set_authors(['maxasix', 'AltServer-Linux and alt-anisette-server', 'made by NyaMisty on Github'])
  about.set_artists(['nebula'])
  about.set_comments("A GUI for AltServer-Linux written in Python.")
  about.set_website("https://github.com/maxasix/AltLinux")
  about.set_website_label("Github")
  about.set_copyright("GUI by maxasix")
  about.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
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
      ermcheck = False

class SplashScreen(Handy.Window):
    def __init__(self):
        super().__init__(title="Loading")
        #self = Gtk.Window(Gtk.WindowType.POPUP)
        self.set_resizable( False )
        #self = Handy.Window(Gtk.WindowType.POPUP)
        self.set_default_size(512, 288)
        self.present()
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.set_keep_above(True)
        # WindowHandle
        self.handle = Handy.WindowHandle()
        self.add(self.handle)                                                                                                                                                

        # WinBox
        self.winBox = Gtk.Box(spacing=0, orientation=Gtk.Orientation.VERTICAL)
        self.handle.add(self.winBox)

        # Revealer
        self.revealer = Gtk.Revealer()
        self.revealer.set_reveal_child(False)
        self.winBox.pack_start(self.revealer, False, True, 0)

        # Headerbar
        self.hb = Handy.HeaderBar()
        self.hb.set_show_close_button(True)
        self.hb.props.title = "AltLinux"
        self.revealer.add(self.hb)

        # MainBox
        self.mainBox = Gtk.Box(spacing=6, orientation=Gtk.Orientation.VERTICAL, halign=Gtk.Align.START, valign=Gtk.Align.START)
        self.winBox.pack_start(self.mainBox, True, False, 0)
        
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
        filename=os.path.join("resources/4.png"), 
        width=512, 
        height=288, 
        preserve_aspect_ratio=False)
        image = Gtk.Image.new_from_pixbuf(pixbuf)
        image.show()
        self.mainBox.pack_start(image, False, True, 0)
        
        self.lbl1 = Gtk.Label("Starting AltLinux...")
        #lbl1.set_property("margin_left", 40)
        #lbl1.set_property("margin_right", 40)
        self.mainBox.pack_start(self.lbl1, False, False, 6)
        self.loadaltlinux = Gtk.ProgressBar()
        #self.progressbar.pulse()
        self.mainBox.pack_start(self.loadaltlinux, True, True, 0)

        GObject.signal_new("my-custom-signal", self, GObject.SignalFlags.RUN_LAST, GObject.TYPE_PYOBJECT,
                       (GObject.TYPE_PYOBJECT,))
        self.connect("my-custom-signal", self.lol321actualfunction)
        self.realthread = threading.Thread(target=self.lol321actualfunction)
        self.realthread.start()

    def lol321actualfunction(self):
      global installedcheck
      command1 = 'echo $XDG_CURRENT_DESKTOP | grep -q "GNOME"'
      #here comes the splash screen
      self.lbl1.set_text("Checking if alt-anisette-server is already running...")
      self.loadaltlinux.set_fraction(0.1)
      subprocess.run("rm /home/$(whoami)/.altlinux/anisettelog.txt",shell=True)
      command = 'curl 127.0.0.1:6969 > "/home/$(whoami)/.altlinux/anisettelog.txt"; grep -q "{" "/home/$(whoami)/.altlinux/anisettelog.txt"'
      CheckRun=subprocess.run(command,shell=True)
      if CheckRun.returncode == 0 :
              print('OK!')
              self.loadaltlinux.set_fraction(0.3)
      else :
              self.lbl1.set_text("Downloading alt-anisette-server... This may take a while")
              self.loadaltlinux.set_fraction(0.3)
              CheckRunA=subprocess.run('id -nG "$USER" | grep -qw docker',shell=True)
              if CheckRunA.returncode == 1 :
                CheckRun3=subprocess.run(f'pkexec sh -c "docker pull nyamisty/alt_anisette_server && docker run -d --rm -p 6969:6969 -it nyamisty/alt_anisette_server"',shell=True)
              else :
                CheckRun3=subprocess.run(f'docker pull nyamisty/alt_anisette_server && docker run -d --rm -p 6969:6969 -it nyamisty/alt_anisette_server',shell=True) 
      self.lbl1.set_text("Starting alt-anisette-server...")
      self.loadaltlinux.set_fraction(0.5)
      finished = False
      global nprogress
      while not finished:
              CheckRun5=subprocess.run(command,shell=True)
              if CheckRun5.returncode == 0 :
                finished = True
              else :
                CheckGrep=subprocess.run(f'grep "Connection refused" "/home/$(whoami)/.altlinux/anisettelog.txt"',shell=True)
                if CheckGrep.returncode == 0 :
                  Gtk.main_quit()
                  os.kill(os.getpid(),signal.SIGKILL)
                else :
                  sleep(3)
              nprogress = nprogress+0.01
              self.loadaltlinux.set_fraction(nprogress)
      CheckCheckRun1 = subprocess.run(f'test -e /home/$(whoami)/.altlinux/AltServer',shell=True)
      if not CheckCheckRun1.returncode == 0:
              self.lbl1.set_text("Downloading AltServer...")
              self.loadaltlinux.set_fraction(nprogress+0.05)
              subprocess.run(f'curl -L https://github.com/NyaMisty/AltServer-Linux/releases/download/v0.0.5/AltServer-x86_64 > /home/$(whoami)/.altlinux/AltServer',shell=True)
              subprocess.run(f'chmod +x /home/$(whoami)/.altlinux/AltServer',shell=True)
      CheckCheckRun2 = subprocess.run(f'test -e /home/$(whoami)/.altlinux/AltStore.ipa',shell=True)
      if not CheckCheckRun2.returncode == 0:
              self.lbl1.set_text("Downloading AltStore...")
              self.loadaltlinux.set_fraction(nprogress+0.05)
              subprocess.run(f'curl -L https://cdn.altstore.io/file/altstore/apps/altstore/1_5_1.ipa > /home/$(whoami)/.altlinux/AltStore.ipa',shell=True)
      self.lbl1.set_text("Starting AltServer...")
      self.loadaltlinux.set_fraction(1.0)
      subprocess.run(f'export ALTSERVER_ANISETTE_SERVER="http://127.0.0.1:6969" & /home/$(whoami)/.altlinux/AltServer &> /dev/null &',shell=True)
      global splcheck
      splcheck = True
      self.emit("my-custom-signal", None)
      return 0

class login(Gtk.Window):
   def __init__(self):
        super().__init__(title="Login")
        self.present()
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.set_resizable( False )
        #self.set_size_request(200, 100)
        self.set_border_width(10)
        
        grid = Gtk.Grid()
        self.add(grid)
        
        #self.set_border_height(20)
        #self.timeout_id = None
        label = Gtk.Label(label="Apple ID: ")
        label.set_justify(Gtk.Justification.LEFT)
        
        self.entry1 = Gtk.Entry()

        label1 = Gtk.Label(label="Password: ")
        label1.set_justify(Gtk.Justification.LEFT)

        self.entry = Gtk.Entry()
        self.entry.set_visibility(False)
        global icon_name
        self.entry.set_icon_from_icon_name(Gtk.EntryIconPosition.SECONDARY, icon_name)
        #self.entry.set_icon_activatable(Gtk.EntryIconPosition.SECONDARY, "view-reveal-symbolic.symbolic")
        self.entry.connect("icon-press", self.on_icon_toggled)

        #self.check_editable = Gtk.CheckButton(label="Editable")
        #self.check_editable.connect("toggled", self.on_editable_toggled)
        #self.check_editable.set_active(True)
        #hbox.pack_start(self.check_editable, True, True, 0)

        #self.check_visible = Gtk.CheckButton(label="Visible")
        #self.check_visible.connect("toggled", self.on_visible_toggled)
        #self.check_visible.set_active(True)
        #hbox.pack_start(self.check_visible, True, True, 0)

        #self.pulse = Gtk.CheckButton(label="Pulse")
        #self.pulse.connect("toggled", self.on_pulse_toggled)
        #self.pulse.set_active(False)
        #hbox.pack_start(self.pulse, True, True, 0)

        #self.icon = Gtk.CheckButton(label="Icon")
        #self.icon.connect("toggled", self.on_icon_toggled)
        #self.icon.set_active(False)
        #hbox.pack_start(self.icon, True, True, 0)

        self.button = Gtk.Button.new_with_label("Login")
        self.button.connect("clicked", self.on_click_me_clicked)
        
        grid.add(label)
        grid.attach(self.entry1, 1, 0, 2, 1)
        grid.attach_next_to(label1, label, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach(self.entry, 1, 2, 1, 1)
        #grid.attach_next_to(self.icon, self.entry, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(self.button, self.entry, Gtk.PositionType.RIGHT, 1, 1)
          
   def on_click_me_clicked(self, button):
        self.entry.set_progress_pulse_step(0.2)
        # Call self.do_pulse every 100 ms
        self.timeout_id = GLib.timeout_add(100, self.do_pulse, None)
        self.entry.set_editable(False)
        self.entry1.set_editable(False)
        self.button.set_sensitive(False)
        GObject.signal_new("my-custom-signal1", self, GObject.SignalFlags.RUN_LAST, GObject.TYPE_PYOBJECT,
                       (GObject.TYPE_PYOBJECT,))
        self.connect("my-custom-signal1", self.onclickmethread)
        self.realthread1 = threading.Thread(target=self.onclickmethread)
        self.realthread1.start()
        #self.realthread1.join()
        Installing = True
        WarnTime=0
        while Installing :  
          CheckIns=subprocess.run(f'grep "Press any key to continue..." {("/home/$(whoami)/.altlinux/log.txt")}',shell=True)
          CheckWarn=subprocess.run(f'grep "Are you sure you want to continue?" {("/home/$(whoami)/.altlinux/log.txt")}',shell=True)
          CheckSuccess=subprocess.run(f'grep "Notify: Installation Succeeded" {("/home/$(whoami)/.altlinux/log.txt")}',shell=True)
          Check2fa=subprocess.run(f'grep "Enter two factor code" {("/home/$(whoami)/.altlinux/log.txt")}',shell=True)
          if CheckIns.returncode == 0 and WarnTime == 1:
              Installing = False
              self.InsAltStore.terminate()
              print('Fail!')
              self.fail()
              self.destroy()  
          if CheckWarn.returncode == 0 and WarnTime == 0 :
                    Installing = False
                    global Warnmsg
                    Warnmsg=subprocess.check_output(f"tail -8 {('/home/$(whoami)/.altlinux/log.txt')}",shell=True).decode()
                    dialog = DialogExample2(self)
                    response = dialog.run()
                    if response == Gtk.ResponseType.OK:
                      dialog.destroy()
                      self.InsAltStore.communicate(input=b'\n')
                      WarnTime = 1
                      Installing = True
                    elif response == Gtk.ResponseType.CANCEL:
                      print('Cancelled. Fail!!')
                      dialog.destroy()
                      self.cancel()

          if Check2fa.returncode == 0 and WarnTime == 0 :
              print("Requires two factor! Awooga!")
              Installing = False
              print("here?")
              dialog = DialogExample(self)
              print("or here?")
              response = dialog.run()
              print("where?")
              if response == Gtk.ResponseType.OK:
                print("huh?")
                vercode = dialog.entry2.get_text()
                print("hm?")
                vercode = vercode+"\n"
                print("yeah?")
                vercodebytes = bytes(vercode.encode())
                print("uh huh?")
                print(vercodebytes)
                print("of course")
                Installing = True
                print("mhm?")
                self.InsAltStore.communicate(input=vercodebytes)
                print("you dont say?")
                dialog.destroy()
              elif response == Gtk.ResponseType.CANCEL:
                print('Cancelled. Fail!')
                self.cancel()
                self.destroy()
          if CheckSuccess.returncode == 0 :
              Installing = False
              print('Success!')
              self.success()
              self.destroy() 
          #self.realthread1.join() 
   def onclickmethread(self):
        AppleID = self.entry1.get_text().lower()
        Password = self.entry.get_text()
        #print(AppleID)
        #print(Password)
        _udid = subprocess.check_output("lsusb -v 2> /dev/null | grep -e 'Apple Inc' -A 2 | grep iSerial | awk '{print $3}'",shell=True).decode().strip()
        _udid_length = len(_udid)
        if _udid_length == 24 :
          UDID = _udid[:8] + '-' + _udid[8:]
        elif _udid_length == 40 :
          UDID = _udid
        self.InsAltStoreCMD=f'''{("export ALTSERVER_ANISETTE_SERVER='http://127.0.0.1:6969' && /home/$(whoami)/.altlinux/AltServer")} -u {UDID} -a {AppleID} -p {Password} {PATH} > {("/home/$(whoami)/.altlinux/log.txt")}'''
        self.InsAltStore=subprocess.Popen(self.InsAltStoreCMD, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

   def success(self):
      self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
      dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text="Success!",
      )
      dialog.format_secondary_text(
            "Operation completed."
      )
      dialog.run()
      print("INFO dialog closed")

      dialog.destroy()

   def cancel(self):
      self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
      dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text="Cancelled",
      )
      dialog.format_secondary_text(
            "Operation cancelled by user"
      )
      dialog.run()
      print("INFO dialog closed")

      dialog.destroy()

   def fail(self):
       self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
       dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.OK,
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

   def on_icon_toggled(self, widget, icon, event):
       global icon_name
       if icon_name == "view-conceal-symbolic.symbolic":
            icon_name = "view-reveal-symbolic.symbolic"
            self.entry.set_visibility(True)
       elif icon_name == "view-reveal-symbolic.symbolic":
            icon_name = "view-conceal-symbolic.symbolic"
            self.entry.set_visibility(False)
       self.entry.set_icon_from_icon_name(Gtk.EntryIconPosition.SECONDARY, icon_name)

class testing(Handy.Window):
    def __init__(self):
        super().__init__(title="Pair your device")
        self.present()
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.set_resizable( False )
        self.set_border_width(20)
        #self.set_default_size(500, 300)

        # WindowHandle
        self.handle = Handy.WindowHandle()
        self.add(self.handle)

        self.hbox = Gtk.Box(spacing=5, orientation=Gtk.Orientation.VERTICAL)
        self.handle.add(self.hbox)
        
        self.hb = Handy.HeaderBar()
        self.hb.set_show_close_button(True)
        self.hb.props.title = "Pair your device"
        self.hbox.pack_start(self.hb, False, True, 0)

        pixbuf = Gtk.IconTheme.get_default().load_icon("phone-apple-iphone-symbolic", 48, 0)
        image = Gtk.Image.new_from_pixbuf(pixbuf)
        image.show()
        image.set_margin_top(5)
        self.hbox.pack_start(image, True, True, 0)
        
        lbl1 = Gtk.Label("Please make sure your device is connected to the computer.\nPress 'Pair' to pair your device.")
        lbl1.set_property("margin_left", 15)
        lbl1.set_property("margin_right", 15)
        lbl1.set_margin_top(5)
        lbl1.set_justify(Gtk.Justification.CENTER)
        self.hbox.pack_start(lbl1, False, False, 0)

        button = Gtk.Button(label="Pair")
        button.connect("clicked", self.on_info_clicked)
        button.set_property("margin_left", 150)
        button.set_property("margin_right", 150)
        self.hbox.pack_start(button, False, False, 10)

        self.add(button)
        self.add(self.hbox)

    def on_info_clicked(self, widget):
        try:
          subprocess.run(['idevicepair pair'], shell=True, check=True)
        except subprocess.CalledProcessError as e:
          print (e.output)
          dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
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
          global PATH
          if lolcheck == "altstr":
            PATH = '/home/$(whoami)/.altlinux/AltStore.ipa'
            win1()
          elif lolcheck == "ipa":
            on_file()
          global ermcheck
          if ermcheck == True:
            PATH = FileChooserWindow().PATHFILE
            win1()
            ermcheck = False
          elif lolcheck == "lol":
            print('OK!!')
          lolcheck = "lol"
        except subprocess.CalledProcessError as e:
          #print (e.output)
          errmoment = e.output
          dialog1 = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.OK,
            #text=e.output,
            text=(errmoment[:-2]),
            #text.select_region(0,-1),
            )
          dialog1.run()
          dialog1.destroy()
        dialog.destroy()
                
class FileChooserWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="FileChooser Example")
        box = Gtk.Box(spacing=6)
        self.add(box)

        dialog = Gtk.FileChooserDialog(
            title="Please choose a file", parent=self, action=Gtk.FileChooserAction.OPEN
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,
            Gtk.ResponseType.OK,
        )

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
            self.PATHFILE = dialog.get_filename()
            global ermcheck
            ermcheck = True
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
            self.destroy()

        dialog.destroy()
        #win4 = login()
        #win4.show_all()

    def add_filters(self, dialog):
        filter_ipa = Gtk.FileFilter()
        filter_ipa.set_name("IPA files")
        filter_ipa.add_pattern("*.ipa")
        dialog.add_filter(filter_ipa)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

class DialogExample(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title="Verification code", transient_for=parent, flags=0)
        self.present()
        self.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK
        )
        self.set_resizable( False )
        #self.set_size_request(200, 100)
        self.set_border_width(10)

        labelhelp = Gtk.Label(label="Enter the verification \ncode on your device: ")
        labelhelp.set_justify(Gtk.Justification.CENTER)

        self.entry2 = Gtk.Entry()

        box = self.get_content_area()
        box.add(labelhelp)
        box.add(self.entry2)
        self.show_all()

class DialogExample2(Gtk.Dialog):
    def __init__(self, parent):
        global Warnmsg
        super().__init__(title="Warning", transient_for=parent, flags=0)
        self.present()
        self.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK
        )
        self.set_resizable( False )
        #self.set_size_request(200, 100)
        self.set_border_width(10)
        # WindowHandle
        handle = Handy.WindowHandle()
        self.add(handle)
        box = Gtk.VBox()
        vb = Gtk.VBox(spacing=0, orientation=Gtk.Orientation.VERTICAL)

        # Headerbar
        self.hb = Handy.HeaderBar()
        self.hb.set_show_close_button(True)
        self.hb.props.title = "Error"
        vb.pack_start(self.hb, False, True, 0)

        labelhelp = Gtk.Label(label="Are you sure you want to continue?")
        labelhelp.set_justify(Gtk.Justification.CENTER)

        labelhelp1 = Gtk.Label(label=Warnmsg)
        labelhelp1.set_justify(Gtk.Justification.CENTER)
        labelhelp1.set_line_wrap(True)
        labelhelp1.set_max_width_chars(48)
        labelhelp1.set_selectable(True)

        #box = self.get_content_area()
        vb.pack_start(labelhelp, False, True, 0)
        vb.pack_start(labelhelp1, False, True, 0)
        self.show_all()

class Oops(Handy.Window):
   def __init__(self):
      super().__init__(title="Error")
      self.present()
      self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
      self.set_resizable( False )
      self.set_size_request(450, 100)
      self.set_border_width(10)	
      # WindowHandle
      handle = Handy.WindowHandle()
      self.add(handle)
      box = Gtk.VBox()
      vb = Gtk.VBox(spacing=0, orientation=Gtk.Orientation.VERTICAL)

      # Headerbar
      self.hb = Handy.HeaderBar()
      self.hb.set_show_close_button(True)
      self.hb.props.title = "Error"
      vb.pack_start(self.hb, False, True, 0)

      pixbuf = Gtk.IconTheme.get_default().load_icon("application-x-addon-symbolic", 48, 0)
      image = Gtk.Image.new_from_pixbuf(pixbuf)
      image.show()
      image.set_margin_top(10)
      vb.pack_start(image, True, True, 0)
      
      lbl1 = Gtk.Label()
      lbl1.set_justify(Gtk.Justification.CENTER)
      lbl1.set_markup(
            "You don't have the AppIndicator extension installed.\nYou can download it on "
            '<a href="https://extensions.gnome.org/extension/615/appindicator-support/" '
            'title="GNOME Extensions">GNOME Extensions</a>.'
        )
      lbl1.set_property("margin_left", 15)
      lbl1.set_property("margin_right", 15)
      lbl1.set_margin_top(10)

      button = Gtk.Button(label="OK")
      button.set_property("margin_left", 125)
      button.set_property("margin_right", 125)
      button.connect("clicked", self.on_info_clicked2)
      
      handle.add(vb)
      vb.pack_start(lbl1, expand = False, fill = True, padding = 0)
      vb.pack_start(button, False, False, 10)
      box.add(vb)
      self.add(box)
      self.show_all()
      
   def on_info_clicked2(self, widget):
     Gtk.main_quit()
     os.kill(os.getpid(),signal.SIGKILL)

class OopsInternet(Handy.Window):
   def __init__(self):
      super().__init__(title="Error")
      self.present()
      self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
      self.set_resizable( False )
      self.set_size_request(450, 100)
      self.set_border_width(10)	
      # WindowHandle
      handle = Handy.WindowHandle()
      self.add(handle)
      box = Gtk.VBox()
      vb = Gtk.VBox(spacing=0, orientation=Gtk.Orientation.VERTICAL)

      # Headerbar
      self.hb = Handy.HeaderBar()
      self.hb.set_show_close_button(True)
      self.hb.props.title = "Error"
      vb.pack_start(self.hb, False, True, 0)

      pixbuf = Gtk.IconTheme.get_default().load_icon("network-wireless-no-route-symbolic", 48, 0)
      image = Gtk.Image.new_from_pixbuf(pixbuf)
      image.show()
      image.set_margin_top(10)
      vb.pack_start(image, True, True, 0)

      lbl1 = Gtk.Label("AltLinux is unable to connect to the Internet.\nPlease connect to the Internet and restart AltLinux.")
      lbl1.set_property("margin_left", 15)
      lbl1.set_property("margin_right", 15)
      lbl1.set_justify(Gtk.Justification.CENTER)
      lbl1.set_margin_top(10)

      button = Gtk.Button(label="OK")
      button.set_property("margin_left", 125)
      button.set_property("margin_right", 125)
      button.connect("clicked", self.on_info_clicked2)
      
      handle.add(vb)
      vb.pack_start(lbl1, expand = False, fill = True, padding = 0)
      vb.pack_start(button, False, False, 10)
      box.add(vb)
      self.add(box)
      self.show_all()
      
   def on_info_clicked2(self, widget):
     Gtk.main_quit()
     os.kill(os.getpid(),signal.SIGKILL)


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
  Gtk.show_uri_on_window(None, "https://github.com/maxasix/AltLinux/releases", Gdk.CURRENT_TIME)
  subprocess.run(f'killall {AltServer}',shell=True)
  Gtk.main_quit()
  os.kill(os.getpid(),signal.SIGKILL)

def on_file():
  win2 = FileChooserWindow()

def lol(_):
  window = testing() 
  window.show_all()

def loloops():
  window = Oops()
  window.connect("destroy", Gtk.main_quit) 
  window.show_all()
  
def loloopsint():
  window = OopsInternet() 
  window.connect("destroy", Gtk.main_quit)
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
    Gtk.show_uri_on_window(None, "https://github.com/maxasix/AltLinux/releases", Gdk.CURRENT_TIME)
    subprocess.run(f'killall {AltServer}',shell=True)
    Gtk.main_quit()
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

def lol321():
  win321 = SplashScreen()
  win321.show_all()

def splashcheck():
  global splcheck
  checked = False
  while not checked:
    if splcheck:
      SplashScreen().destroy()
    else:
      sleep(3)
def quit(_):
  subprocess.run(f'killall {AltServer}',shell=True)
  Gtk.main_quit()
  os.kill(os.getpid(),signal.SIGKILL)
  
if __name__ == "__main__":
  main()
