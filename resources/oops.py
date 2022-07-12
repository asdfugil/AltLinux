#!/usr/bin/python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk as gtk
from gi.repository import GLib

class testing(gtk.Window):

   def __init__(self):
      super().__init__(title="Error")
      self.present()
      self.set_position(gtk.WindowPosition.CENTER_ALWAYS)
      self.set_resizable( False )
      self.set_size_request(450, 100)
      self.set_border_width(10)	
      box = gtk.VBox()
      vb = gtk.VBox()
      lbl = gtk.Label("Oops!")
      lbl.set_justify(gtk.Justification.CENTER)
      lbl1 = gtk.Label("You don't have the AppIndicator extension installed.")
      lbl1.set_justify(gtk.Justification.CENTER)
      lbl2 = gtk.Label()
      lbl2.set_markup(
            "You can download it on "
            '<a href="https://extensions.gnome.org/extension/615/appindicator-support/" '
            'title="GNOME Extensions">GNOME Extensions</a>.'
        )
      lbl2.set_justify(gtk.Justification.CENTER)
      button = gtk.Button(label="OK")
      button.connect("clicked", self.on_info_clicked)
      
      vb.pack_start(lbl, expand = True, fill = True, padding = 0)
      vb.pack_start(lbl1, expand = True, fill = True, padding = 0)
      vb.pack_start(lbl2, expand = True, fill = True, padding = 0)
      vb.pack_start(button, False, False, 10)
      box.add(vb)
      self.add(box)
      self.show_all()
      
   def on_info_clicked(self, widget):
     gtk.main_quit()

GLib.set_prgname('AltLinux')
testing()
gtk.main()
