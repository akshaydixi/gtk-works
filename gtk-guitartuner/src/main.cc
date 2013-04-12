/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- */
/*
 * main.cc
 * Copyright (C) 2012 Akshay <akshay@ak42>
 * 
 * gtk-guitartuner is free software: you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as published
 * by the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * gtk-guitartuner is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU Lesser General Public License for more details.
 * 
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.";
 */

#include <gtkmm.h>
#include <iostream>
#include <gstreamermm.h>
#include "config.h"


#ifdef ENABLE_NLS
#  include <libintl.h>
#endif



/* For testing propose use the local (not installed) ui file */
/* #define UI_FILE PACKAGE_DATA_DIR"/ui/gtk_guitartuner.ui" */
class Sound
{
	public:
		Sound();

		void start_playing(double frequency);
		bool stop_playing();
	private:
		Glib::RefPtr<Gst::Pipeline> m_pipeline;
		Glib::RefPtr<Gst::Element> m_source;
		Glib::RefPtr<Gst::Element> m_sink;

};

Sound::Sound()
{
	m_pipeline = Gst::Pipeline::create("note");
	m_source = Gst::ElementFactory::create_element("audiotestsrc",
	                                               "source");
	m_sink = Gst::ElementFactory::create_element ("autoaudiosink",
	                                              "output");
	m_pipeline  -> add(m_source);
	m_pipeline  -> add(m_sink);
	m_source -> link(m_sink);
}

void Sound::start_playing (double frequency)
{
	m_source -> set_property("freq",
	                         frequency);
	m_pipeline -> set_state (Gst::STATE_PLAYING);

	Glib::signal_timeout ().connect(sigc::mem_fun(*this,&Sound::stop_playing),
	                                200);
}

bool Sound::stop_playing ()
{
	m_pipeline -> set_state(Gst::STATE_NULL);
	return false;
}

static void
on_button_clicked(double frequency, Sound* sound)
{
	sound->start_playing (frequency);
}

   
int
main (int argc, char *argv[])
{
	Gtk::Main kit(argc, argv);
	

	//Load the Glade file and instiate its widgets:
	Glib::RefPtr<Gtk::Builder> builder;
	try
	{
		builder = Gtk::Builder::create_from_file(UI_FILE);
	}
	catch (const Glib::FileError & ex)
	{
		std::cerr << ex.what() << std::endl;
		return 1;
	}
	Gst::init(argc,argv);
	Gtk::Window* main_win = 0;
	builder->get_widget("main_window", main_win);
	Sound sound;
	Gtk::Button* button;
	builder->get_widget("button_E",button);
	button->signal_clicked().connect (sigc::bind<double, Sound*>(sigc::ptr_fun(&on_button_clicked),
	                                                             369.23,&sound));   

	if (main_win)
	{
		kit.run(*main_win);
	}
	return 0;
}
