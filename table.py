from gi.repository import Gtk
class App(object):
    def __init__(self):
        window = Gtk.Window()
        window.set_title('Example')
        window.connect('delete-event',Gtk.main_quit)
        table = Gtk.Table(3,3,True)
        button_1 = Gtk.Button('Button 1')
        button_2 = Gtk.Button('Button 2')
        button_3 = Gtk.Button('Button 3')
        button_4 = Gtk.Button('Button 4')
        button_5 = Gtk.Button('Button 5')
        label = Gtk.Label()
        label.set_markup('Vist us at this <a href = "http://www.facebook.com/akshay.dixi/">page</a>')
        table.attach(button_1,0,1,0,1)
        table.attach(button_2,1,3,0,1)
        table.attach(button_3,0,1,1,3)
        table.attach(button_4,1,3,1,2)
        table.attach(button_5,1,2,2,3)
        table.attach(label,2,3,2,3)
        button_1.connect('clicked',self.on_button_clicked)
        button_2.connect('clicked',self.on_button_clicked)
        button_3.connect('clicked',self.on_button_clicked)
        button_4.connect('clicked',self.on_button_clicked)
        button_5.connect('clicked',self.on_button_clicked)
        #button_6.connect('clicked',self.on_button_clicked)
        window.add(table)
        window.show_all()
        Gtk.main()

    def on_button_clicked(self,button):
        print button.get_label()+' clicked!!'
App()
