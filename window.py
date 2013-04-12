#!/usr/bin/env python
from gi.repository import Gtk

def main():
	window = Gtk.Window()
	window.set_title('Hello World')
	window.set_default_size(300,200)
	window.set_position(Gtk.WindowPosition.CENTER)
	window.connect('destroy',destroy)
	button = Gtk.Button('Press Me!!')
	button.connect_after('clicked',button_clicked)
	window.add(button)
	window.show_all()
	Gtk.main()
def destroy(window):
	Gtk.main_quit()
def button_clicked(button):
	print 'Clicked!!'

if __name__ == '__main__':
	main()

