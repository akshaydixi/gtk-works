from gi.repository import Gtk,Gdk
import sys,os
import sqlite3
class handler:
    connection = sqlite3.connect('/home/akshay/yetAnotherWorkspace/pokedex/db/veekun-pokedex.sqlite')
    cursor = connection.cursor()
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('/home/akshay/yetAnotherWorkspace/glade/pokedex-0_2.glade')
        self.builder.get_object('window1').show_all()
        self.builder.connect_signals(self)
        self.directory = '/home/akshay/yetAnotherWorkspace/pokedex/sprites/sugimori'
        self.photos = os.listdir(self.directory)
        self.photos.remove('0female')
        self.photos.sort()
        self.position = 0
        self.image = self.builder.get_object('image1')
        self.image2 = self.builder.get_object('image2')
        self.image3 = self.builder.get_object('image3')
        self.label1 = self.builder.get_object('label1')
        self.label2 = self.builder.get_object('label2')
        self.label3 = self.builder.get_object('label3')
        self.label4 = self.builder.get_object('label4')
        self.achange(0); 
        Gtk.main()

    def on_key_pressed(self,widget,event):
      if event.keyval == Gdk.KEY_Right:
        self.achange(1)
      elif event.keyval == Gdk.KEY_Left:
        self.achange(-1)
    
    def destroy(self,*args):
        Gtk.main_quit(*args)
    def on_button_clicked(self,args):
        label = args.get_label()
        if label == 'gtk-media-next':
            self.achange(1)
        else:
            self.achange(-1)
        #print label
    def achange(self,ch):
            self.position = (self.position + ch) % len(self.photos)
            self.image.set_from_file(os.path.join(self.directory,self.photos[self.position]))
            self.labelize(self.photos[self.position][0:3])
    def labelize(self,num):
        self.cursor.execute('select pokemon_species_id,pokemon_species_names.name,genus,type_names.name from pokemon_species_names,pokemon_types,type_names where(pokemon_species_names.local_language_id = 9 AND pokemon_species_names.local_language_id=type_names.local_language_id AND type_names.type_id = pokemon_types.type_id AND pokemon_species_names.pokemon_species_id = pokemon_types.pokemon_id AND pokemon_species_id = '+num+');')
        result = self.cursor.fetchall()
        print result    
        self.label1.set_text('ID   : # '+str(result[0][0]))
        self.label2.set_text('NAME :   '+result[0][1])
        self.label3.set_text('    '+result[0][2]+' Pokemon')
        self.label4.set_text('TYPE : ')
        self.image2.set_from_file('/home/akshay/yetAnotherWorkspace/pokedex/sprites/types/'+result[0][3]+'.png')
        if(len(result)>1):
            self.image3.set_from_file('/home/akshay/yetAnotherWorkspace/pokedex/sprites/types/'+result[1][3]+'.png')
        else:
            self.image3.set_from_stock(Gtk.STOCK_DISCARD,1)    
if __name__ == '__main__':
    handler()
