from gi.repository import Gtk
class Test():
    def __init__(self):
        win = Gtk.Window()
        win.set_title("Hello World")
        box = Gtk.Box()
        button = Gtk.Button('Button 1')
        button.connect('clicked',self.on_clicked_event)
        box.pack_start(button,True,True,5)
        button = Gtk.Button('Button 2')
        button.connect('clicked',self.on_clicked_event)
        box.pack_start(button,True,True,5)
        win.add(box)
        win.show_all()
        win.connect('delete-event',Gtk.main_quit)
        Gtk.main()
    def on_clicked_event(self,button):
        if(button.get_label() == 'Button 1'):
            print 'Button 1 pressed'
        else:
            print 'Button 2 pressed'
Test()
