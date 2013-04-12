from gi.repository import Gtk
class Test():
 def __init__(self):
            win = Gtk.Window()
            button = Gtk.Button('Click Me')
            button.connect_after('clicked',self.click)
            win.connect_after('delete-event',Gtk.main_quit)
            win.add(button)
            win.show_all()
            Gtk.main()
 def click(self,button):
           if(button.get_label() == 'Click Me'):
             button.set_label('Press Me')
           else:
             button.set_label('Click Me')

       
Test()
          
            
