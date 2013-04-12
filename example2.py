from gi.repository import Gtk
import os,sys
import sqlite3

directory = '/home/akshay/yetAnotherWorkspace/'


class initialize():
  def __init__(self):
    self.connection = sqlite3.connect(directory + '/pokedex/db/veekun-pokedex.sqlite')
    self.cursor = self.connection.cursor()
    self.cursor.execute('select pokemon_species_id,pokemon_species_names.name,genus from pokemon_species_names where(pokemon_species_names.local_language_id = 9 )')
    result = self.cursor.fetchall()
    store = Gtk.ListStore(int,str,str)
    
    for i in range(len(result)):
      treeiter = store.append(result[i])
    for row in store:
      print row[:]
    self.entry = Gtk.Entry()
    
    self.filter = store.filter_new()
    self.filter.set_visible_func(self.filter_function,data=None)
    self.storesort = Gtk.TreeModelSort(model=self.filter)
    tree = Gtk.TreeView(model=self.storesort)
    self.model = tree.get_model()
    renderer = Gtk.CellRendererText()
    renderer2=Gtk.CellRendererText()
    renderer3=Gtk.CellRendererText()
    column = Gtk.TreeViewColumn('#',renderer,text=0)
    column2=Gtk.TreeViewColumn('name',renderer2,text=1)
    column3=Gtk.TreeViewColumn('genus',renderer3,text=2)
    tree.append_column(column)
    tree.append_column(column2)
    self.select = tree.get_selection()
    self.select.connect('changed',self.on_tree_selection_changed)
    window = Gtk.Window()
    self.entry.connect('activate',self.search,)
    box = Gtk.Box()    
    hbox = Gtk.Box()
    hbox.set_orientation(Gtk.Orientation.VERTICAL)
    hbox.add(self.entry)
    hbox.add(box)
    scrolledwindow = Gtk.ScrolledWindow(shadow_type = Gtk.ShadowType.IN)
    scrolledwindow.set_hexpand(True)
    scrolledwindow.set_vexpand(True)
    scrolledwindow.add(tree)
    self.image = Gtk.Image()
    self.image.set_from_file(directory+'pokedex/sprites/sugimori/001.png')
    window.add(hbox)
    box.add(scrolledwindow)
    box.add(self.image)
    window.connect('delete-event',Gtk.main_quit)
    window.set_size_request(600,400)
    window.show_all()
    Gtk.main()

  def on_tree_selection_changed(self,select):
    model,treeiter = select.get_selected()
    image_name = str(model[treeiter][0])
    while(len(image_name)<3):
      image_name = '0'+image_name
    image_name +='.png'    
    self.image.set_from_file(directory+'pokedex/sprites/sugimori/'+image_name)
    
  def search(self,entry):
    self.filter.refilter()
    self.select.select_iter(self.model.get_iter_first())
    
  def filter_function(self,model,iter,query):
    if(self.entry.get_text() == None):
      return True
    check = model[iter][1].lower()
    if str(self.entry.get_text()) in str(check):
      return True
    return False
        
initialize()
    
