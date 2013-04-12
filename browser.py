from gi.repository import Gtk,WebKit
import sys,os

class Browser(object):
  def __init__(self):
    window = Gtk.Window()
    window.set_title('Browser')
    window.set_position(Gtk.WindowPosition.CENTER)
    window.set_size_request(300,300)
    window.connect('delete-event',Gtk.main_quit)
    box = Gtk.Box()
    box.set_orientation(Gtk.Orientation.VERTICAL)
    entry = Gtk.Entry()
    entry.connect('activate',self.change_url)
    box.pack_start(entry,False,False,5)
    self.webview = WebKit.WebView()
    box.pack_start(self.webview,True,True,5)
    window.add(box)
    window.show_all()
    Gtk.main()
  
  def change_url(self,entry):
    print entry.get_text()
    self.webview.open(entry.get_text())
  
Browser()  
