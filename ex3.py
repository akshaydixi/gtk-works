from gi.repository import Gtk
import os
import sys

class PhotoChooser():
    def __init__(self):
        window = Gtk.Window()
        window.set_title("Photo Chooser")
        window.set_position(Gtk.WindowPosition.CENTER)
        window.connect('destroy',Gtk.main_quit)
        self.box = Gtk.Box()
        self.box.set_orientation(Gtk.Orientation.VERTICAL)
        self.image = Gtk.Image()
        self.box.add(self.image)
        button = Gtk.Button("Open Photo..")
        self.box.add(button)
        button.connect('clicked',self.on_button_clicked)
        window.add(self.box)
        window.show_all()

    def on_button_clicked(self,args):
        dialog = Gtk.FileChooserDialog('Choose a photo',args.get_toplevel(),Gtk.FileChooserAction.OPEN)
        dialog.add_button(Gtk.STOCK_CANCEL,0)
        dialog.add_button(Gtk.STOCK_OPEN,1)
        dialog.set_default_response(1)

        filefilter = Gtk.FileFilter()
        filefilter.add_pixbuf_formats()
        dialog.set_filter(filefilter)

        if dialog.run() == 1:
            self.image.set_from_file(dialog.get_filename())
        dialog.destroy()

def main():
    PhotoChooser()
    Gtk.main()

if __name__ == '__main__':
    main()

