from gi.repository import Gtk
# help from http://python-gtk-3-tutorial.readthedocs.org/en/latest/builder.html
#import Gtk.builder

builder = Gtk.Builder()

builder.add_from_file("MainWindow.glade")

MainWindow = builder.get_object("MainWindow")
ToggleServerBtn = builder.get_object("ToggleServerOn")

#define functions here
class Handler():
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)
    def ToggleServerOnPreon_ToggleServerOn_toggledss():
        print("hello World!")
        return 1

    def ToggleServerOn_toggled_cb():
        pass
    
#link signals to functions here - No LOOPS ALLOWED without a sub process
###handlers = {
###    "onDeleteWindow": Gtk.main_quit,
###    "on_ToggleServerOn_toggled": ToggleServerOnPress,
###    "ToggleServerOn_toggled_cb": ToggleServerOnDepress,
###}
builder.connect_signals(Handler())

#Display window once loaded.
MainWindow.show_all()

Gtk.main()
