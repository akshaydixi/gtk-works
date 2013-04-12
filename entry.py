from gi.repository import Gtk,GObject
class entrydemo():
    def __init__(self):
        self.timeout_id = None
        window = Gtk.Window()
        window.set_title('Entry Demo')
        window.set_size_request(200,100)
        window.connect('destroy',Gtk.main_quit)
        
        vbox = Gtk.Box()
        vbox.set_spacing(6)
        vbox.set_orientation(Gtk.Orientation.VERTICAL)
        
        self.entry = Gtk.Entry()
        self.entry.set_can_focus(False)
        vbox.pack_start(self.entry,True,True,0)
        
        hbox = Gtk.Box()
        hbox.set_spacing(6)
        vbox.pack_start(hbox,True,True,0)
        
        self.editable = Gtk.CheckButton('Editable')
        self.editable.connect('toggled',self.on_editable_toggled)
        hbox.pack_start(self.editable,True,True,0)
        
        self.visible = Gtk.CheckButton('Visible')
        self.visible.connect('toggled',self.on_visible_toggled)
        hbox.pack_start(self.visible,True,True,0)
        
        self.pulse = Gtk.CheckButton('Pulse')
        self.pulse.connect('toggled',self.on_pulse_toggled)
        hbox.pack_start(self.pulse,True,True,0)
        
        self.icon = Gtk.CheckButton('Icon')
        self.icon.connect('toggled',self.on_icon_toggled)
        hbox.pack_start(self.icon,True,True,0)
        window.add(vbox)
        window.show_all()
        Gtk.main()
        
    def on_editable_toggled(self,toggle):
        print 'Editable toggled'
        value = toggle.get_active()
        self.entry.set_editable(value)
        
    def on_visible_toggled(self,toggle):
        print 'Visible toggled'
        value = toggle.get_active()
        self.entry.set_visibility(value)
    
    def on_pulse_toggled(self,toggle):
        print 'Pulse toggled'
        if toggle.get_active():
            self.entry.set_progress_pulse_step(0.005)
            self.timeout_id = GObject.timeout_add(5,self.do_pulse,None)
        else:
            GObject.source_remove(self.timeout_id)
            self.timeout_id = None
            self.entry.set_progress_pulse_step(0)
            
    def do_pulse(self,data):
        self.entry.progress_pulse()
        return True
    
    
    def on_icon_toggled(self,toggle):
        print 'Icon toggled'
        if toggle.get_active():
            stock_id = Gtk.STOCK_FIND
        else:
            stock_id = None
        self.entry.set_icon_from_stock(Gtk.EntryIconPosition.PRIMARY,stock_id)
        
if __name__ == '__main__':
    entrydemo()
