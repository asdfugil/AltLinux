#!/usr/bin/python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk as gtk
from gi.repository import GLib
from gi.repository import Gdk

class testing(gtk.Window):

   def __init__(self):
      super().__init__(title="AltLinux")
      self.present()
      self.set_position(gtk.WindowPosition.CENTER_ALWAYS)
      self.set_resizable( False )
      self.set_size_request(200, 100)
      self.set_border_width(10)	
      box = gtk.VBox()
      vb = gtk.VBox()
      lbl = gtk.Label()
      lbl.set_markup(
            "<big>Please wait...</big>"
        )
      lbl.set_justify(gtk.Justification.CENTER)
      vb.pack_start(lbl, expand = True, fill = True, padding = 10)
      #self.progressbar = gtk.ProgressBar()
      #self.progressbar.pulse()
      #vb.pack_start(self.progressbar, True, True, 5)
      self.spinner = gtk.Spinner()
      self.spinner.start()
      vb.pack_start(self.spinner, True, True, 5)
      box.add(vb)
      self.add(box)
      self.show_all()
      #self.set_decorated(False)

GLib.set_prgname('AltLinux')
testing()
gtk.main()
