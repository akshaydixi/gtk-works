from gi.repository import Gtk
import os
import sys

class PhotoBrowser():
    def __init__(self):
        self.window = Gtk.Window()
        self.window.set_title('Pokedex')
        self.window.set_position(Gtk.WindowPosition.CENTER)
        self.window.connect('destroy',Gtk.main_quit)
        vbox = Gtk.Box()
        vbox.set_spacing(5)
        self.window.add(vbox)
        vbox.set_orientation(Gtk.Orientation.VERTICAL)
        #self.directory = self.getdir()
        self.directory = '/home/akshay/yetAnotherWorkspace/pokedex/sprites/sugimori'
        self.photos = os.listdir(self.directory)
        self.photos.sort()
        
        self.position = 0
        self.image = Gtk.Image()
        self.image.set_from_file(os.path.join(self.directory,self.photos[0]))
        vbox.add(self.image)
        hbox = Gtk.Box(homogeneous = True)
        vbox.pack_end(hbox,False,False,5)
        button1 = Gtk.Button.new_from_stock('gtk-media-previous')
        button2 = Gtk.Button.new_from_stock('gtk-media-next')
        button1.connect_after('clicked',self.change,-1)
        button2.connect_after('clicked',self.change,1)
        hbox.add(button1)
        hbox.add(button2)
        
        self.window.show_all()


    def change(self,button,data):
        self.position = (self.position + data) % len(self.photos)
        self.image.set_from_file(os.path.join(self.directory,self.photos[self.position]))
        

    def getdir(self):
        dialog = Gtk.FileChooserDialog('Choose a folder',self.window,Gtk.FileChooserAction.SELECT_FOLDER)
        dialog.add_button(Gtk.STOCK_CANCEL,0)
        dialog.add_button(Gtk.STOCK_OPEN,1)
        dialog.set_default_response(1)

        if dialog.run() == 1:      
            path = dialog.get_filename()
            dialog.destroy()
            return path

start = PhotoBrowser()
Gtk.main()



