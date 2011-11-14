#!/usr/bin/env python

from gi.repository import Gio, Gtk

class App:
    BASE_KEY = "org.gnome.shell.extensions.musicintegration"
    def __init__(self):
	settings = Gio.Settings.new(self.BASE_KEY)
	nswitch = Gtk.Switch()

	window = Gtk.Window()
        window.connect('destroy', lambda w: Gtk.main_quit())
	window.set_title('Music Integration Preferences')
	window.set_default_size(400, 160)	
	window.set_border_width(6)

	window.set_position(Gtk.WindowPosition.CENTER)
	
	mainvbox = Gtk.VBox(spacing=6)
	window.add(mainvbox)
	
	mainhbox = Gtk.HBox()
	mainvbox.add(mainhbox)
	
	spacebox1 = Gtk.HBox()
	mainhbox.add(spacebox1)
	spacebox1.set_size_request(30,0)
        
	vbox = Gtk.VBox()
	mainhbox.add(vbox)
	
	spacebox2 = Gtk.HBox()
	mainhbox.add(spacebox2)
	spacebox2.set_size_request(30,0)

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
        player.append_text('Player as Indicator in Panel')
        player.append_text('Player in Volume Menu')
        player.append_text('Notifications only')
        player.connect('changed', self.keys_change, settings, nswitch)
        player.set_active(int(settings.get_string("setup")))
        player.set_size_request(300, 0)


	nlabel1 = Gtk.Label("")
	vbox.pack_start(nlabel1, False, True, 0)
	
	nhbox = Gtk.Box(spacing=0)
	vbox.pack_start(nhbox, False, True, 0)
	nhbox.set_size_request(300, 30)
	
	nlabel = Gtk.Label("Notifications")
	nhbox.pack_start(nlabel, False, True, 0)
	
	nswitch.set_active(settings.get_boolean("notification"))
	nswitch.connect('notify::active', self.n_change, settings)
	nhbox.pack_end(nswitch, False, True, 0)

	
	cohbox = Gtk.Box(spacing=0)
	vbox.pack_start(cohbox, False, True, 0)
	cohbox.set_size_request(300, 30)
	
	colabel = Gtk.Label("Cover Art Time Overlay")
	cohbox.pack_start(colabel, False, True, 0)
	
	coswitch = Gtk.Switch()
	coswitch.set_active(settings.get_boolean("overlay"))
	coswitch.connect('notify::active', self.co_change, settings)
	cohbox.pack_end(coswitch, False, True, 0)
	
	
	emptylabel = Gtk.Label("")
	mainvbox.add(emptylabel)

	quithbox = Gtk.HBox()
	mainvbox.add(quithbox)

	quitbutton = Gtk.Button("Quit")
        quitbutton.connect("clicked", Gtk.main_quit )
	quithbox.pack_start(quitbutton, False, True, 0)
	
	quitalign = Gtk.Align(2)
	quithbox.set_halign(quitalign)

        window.show_all()

        return

    def keys_change(self, player, settings, nswitch):
        index = player.get_active()
        if index == 3:
            nswitch.set_active(True)
            nswitch.set_sensitive(False)
        else:
            nswitch.set_active(settings.get_boolean("notification"))
            nswitch.set_sensitive(True)
        settings.set_string("setup", str(player.get_active()))
        return

    def co_change(self, coswitch, value, settings):
        settings.set_boolean("overlay", coswitch.get_active())
        return

    def n_change(self, coswitch, value, settings):
        settings.set_boolean("notification", coswitch.get_active())
        return

def main():
    Gtk.main()
    return

if __name__ == "__main__":
    app = App()
    main()
