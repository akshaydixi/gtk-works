#include<gtk/gtk.h>

gint
button_counter=0;
static void
print_me (GtkWidget* widget,
	  gpointer data)
{
g_print("Button Pressed %d times\n",++button_counter);
}

static void
push_me(GtkEntry *widget,
	gpointer data)
{
g_print("Hello %s\n",gtk_entry_get_text(widget));
}

int 
main (int argc,
      char *argv[])
{
GtkWidget *window;
GtkWidget *button;
GtkWidget *grid;
GtkWidget *button1;
gtk_init(&argc,&argv);

window = gtk_window_new(GTK_WINDOW_TOPLEVEL);

g_signal_connect(window,"destroy",G_CALLBACK(gtk_main_quit),NULL);

gtk_container_set_border_width(GTK_CONTAINER(window),10);

grid = gtk_grid_new();

gtk_container_add(GTK_CONTAINER(window),grid);

button = gtk_button_new_with_label("Press Me!");

g_signal_connect(button,"clicked",G_CALLBACK(print_me),NULL);

gtk_grid_attach(GTK_GRID(grid),button,0,0,2,1);

button = gtk_button_new_with_label("Quit");

g_signal_connect_swapped(button,"clicked",G_CALLBACK(gtk_widget_destroy),window);

gtk_grid_attach(GTK_GRID(grid),button,0,1,2,1);

button1 = gtk_entry_new();

gtk_entry_set_placeholder_text(GTK_ENTRY(button1),"Enter your name here: ");

gtk_grid_attach(GTK_GRID(grid),button1,0,2,2,1);

button = gtk_button_new_with_label("Push me");

g_signal_connect_swapped(button,"clicked",G_CALLBACK(push_me),button1);

gtk_grid_attach(GTK_GRID(grid),button,0,3,2,1);

gtk_widget_show_all(window);

gtk_main();

return 0;

}


