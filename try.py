from gi.repository import Gtk,Gst,GObject
import os,sys
class Test (object):
	def __init__(self):
		Gst.init_check(sys.argv)
		self.builder = Gtk.Builder()
		self.builder.add_from_file("/home/akshay/yetAnotherWorkspace/glade/saregama.glade")
		self.builder.connect_signals(self)
	def run(self,*args):
		self.builder.get_object("window1").show()	
		Gtk.main()

	options={'Sa':240,'Re':270,'Ga':300,'Ma':320,'Pa':360,'Dha':400,'Ni':450,'SA':480}
		
	def on_button_clicked(self,button):
		self.play_sound(self.options[button.get_label()])

	def quit(self,*args):
		Gtk.main_quit()

	def play_sound(self,frequency):
		pipeline=Gst.Pipeline(name='note')
		source=Gst.ElementFactory.make('audiotestsrc','src')
		sink=Gst.ElementFactory.make('autoaudiosink','output')
		source.set_property('freq',frequency)
		pipeline.add(source)
		pipeline.add(sink)
		source.link(sink)
		pipeline.set_state(Gst.State.PLAYING)
		GObject.timeout_add(self.LENGTH,self.pipeline_stop,pipeline)
	def pipeline_stop(self,pipeline):
		pipeline.set_state(Gst.State.PAUSED)
		return False
	LENGTH = 500
Test().run()
