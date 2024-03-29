#include<gtk/gtk.h>
static void
print_hello (GtkWidget *widget,
	gpointer data)
{
g_print ("Hello World\n");
}

int
main (int argc,
	char *argv[])
{
GtkWidget *button;

GtkWidget *window;

GtkWidget *grid;

gtk_init(&argc,&argv);

window = gtk_window_new(GTK_WINDOW_TOPLEVEL);

gtk_window_set_title(GTK_WINDOW(window),"Grid");

g_signal_connect(window,"destroy",G_CALLBACK(gtk_main_quit),NULL);

gtk_container_set_border_width(GTK_CONTAINER(window),10);

grid = gtk_grid_new();

gtk_container_add(GTK_CONTAINER(window),grid);

button = gtk_button_new_with_label("Button 1");

g_signal_connect(button,"clicked",G_CALLBACK(print_hello),NULL);

gtk_grid_attach(GTK_GRID(grid),button,0,0,1,1);

button = gtk_button_new_with_label("Button 2");

g_signal_connect(button,"clicked",G_CALLBACK(print_hello),NULL);

gtk_grid_attach(GTK_GRID(grid),button,1,0,1,1);

button = gtk_button_new_with_label("Quit");

g_signal_connect(button,"clicked",G_CALLBACK(gtk_main_quit),NULL);

gtk_grid_attach(GTK_GRID(grid),button,0,1,2,1);

gtk_widget_show_all(window);

gtk_main();

return 0;

}
