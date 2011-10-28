#!/usr/bin/env python

from gi.repository import Gio, Gtk

class App:
    BASE_KEY = "org.gnome.shell.extensions.musicintegration"
    def __init__(self):
	settings = Gio.Settings.new(self.BASE_KEY)

	window = Gtk.Window()
        window.connect('destroy', lambda w: Gtk.main_quit())
	window.set_title('Music Integration Preferences')
	window.set_default_size(400, 160)	
	window.set_border_width(6)

	window.set_position(Gtk.WindowPosition.CENTER)
        
	vbox = Gtk.VBox(spacing=6)
	window.add(vbox)

	label = Gtk.Label("")
	vbox.pack_start(label, False, True, 0)
	labelT = Gtk.Label("Choose your default setup :")
	vbox.pack_start(labelT, False, True, 0)
	
	hplayerbox = Gtk.HBox(spacing=0)
	vbox.pack_start(hplayerbox, False, True, 0)
	hpalign = Gtk.Align(3)
	hplayerbox.set_halign(hpalign)

	player = Gtk.ComboBoxText()
        
	hplayerbox.pack_start(player, False, True, 0)
        player.append_text('Choose a setup :')
        player.append_text('Panel and Notifications')
        player.append_text('Panel Indicator only')
        player.append_text('Notifications only')
        player.connect('changed', self.keys_change, settings)
        player.set_active(int(settings.get_string("setup")))
        player.set_size_request(300, 30)

	label1 = Gtk.Label("")
	vbox.pack_start(label1, False, True, 0)

	hbox = Gtk.HBox(spacing=6)
	vbox.add(hbox)

	label3 = Gtk.Label("")
	hbox.pack_start(label3, False, True, 0)

	button = Gtk.Button("Quit")
        button.connect("clicked", Gtk.main_quit )
	hbox.pack_start(button, False, True, 0)
	
	align = Gtk.Align(2)
	hbox.set_halign(align)

        window.show_all()

        return

    def keys_change(self, player,settings):
        index = player.get_active()
        if index:
		settings.set_string("setup", str(player.get_active()))
        return

def main():
    Gtk.main()
    return

if __name__ == "__main__":
    app = App()
    main()
