#!/usr/bin/env python

from gi.repository import Gio, Gtk
import gettext

TRANSLATION_DOMAIN = "gnome-shell-extension-musicintegration"

gettext.install(TRANSLATION_DOMAIN)


class App:

    BASE_KEY = "org.gnome.shell.extensions.musicintegration"

    def __init__(self):
        settings = Gio.Settings.new(self.BASE_KEY)
        nswitch = Gtk.Switch()

        window = Gtk.Window()
        window.connect('destroy', lambda w: Gtk.main_quit())
        window.set_title(_('Music Integration Preferences'))
        window.set_icon_name(Gtk.STOCK_PREFERENCES)
        window.set_default_size(400, 100)        
        window.set_border_width(10)

        window.set_position(Gtk.WindowPosition.CENTER)

        mainvbox = Gtk.VBox(spacing=6)
        window.add(mainvbox)

        mainhbox = Gtk.HBox()
        mainvbox.add(mainhbox)

        vbox = Gtk.VBox()
        mainhbox.add(vbox)

        hplayerbox = Gtk.Box(spacing=0)
        vbox.pack_start(hplayerbox, False, True, 0)

        labelT = Gtk.Label(_("Place indicator as:"))
        hplayerbox.pack_start(labelT, False, True, 0)

        player = Gtk.ComboBoxText()
        # TODO: This option should be dropped
        player.append_text(_('Indicator in Panel'))
        player.append_text(_('Part of the Volume Menu'))
        player.append_text(_('Don\'t show indicator'))
        player.connect('changed', self.keys_change, settings, nswitch)
        player.set_active(int(settings.get_string("setup")))
        hplayerbox.pack_end(player, False, True, 2)

        label = Gtk.Label("")
        vbox.pack_start(label, False, True, 0)

        nhbox = Gtk.Box(spacing=0)
        vbox.pack_start(nhbox, False, True, 0)
        # nhbox.set_size_request(300, 30)

        nlabel = Gtk.Label(_("Show notifications"))
        nhbox.pack_start(nlabel, False, True, 0)

        nswitch.set_active(settings.get_boolean("notification"))
        nswitch.connect('notify::active', self.n_change, settings)
        nhbox.pack_end(nswitch, False, True, 2)

        cohbox = Gtk.Box(spacing=0)
        vbox.pack_start(cohbox, False, True, 0)

        colabel = Gtk.Label(_("Show play time over cover art"))
        cohbox.pack_start(colabel, False, True, 0)

        coswitch = Gtk.Switch()
        coswitch.set_active(settings.get_boolean("overlay"))
        coswitch.connect('notify::active', self.co_change, settings)
        cohbox.pack_end(coswitch, False, True, 2)

        quithbox = Gtk.HBox()
        mainvbox.add(quithbox)

        quitbutton = Gtk.Button(_("Quit"))
        quitbutton.connect("clicked", Gtk.main_quit)
        quithbox.pack_start(quitbutton, False, True, 0)

        quitalign = Gtk.Align(2)
        quithbox.set_halign(quitalign)

        window.show_all()

        return

    def keys_change(self, player, settings, nswitch):
        index = player.get_active()
        if index == 2:
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
