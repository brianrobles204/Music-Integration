## Music Integration Extension
Integrate your music with the Gnome Shell.

This extension listens to Dbus MPRIS2 and automatically looks for players. It then adds an icon to the 
Gnome panel when it finds a music player and creates a nice notification when the song changes.
You also have an option to integrate the player into the volume menu, much like in Ubuntu's setup.
All these options are configurable through a nice GUI tool.

Supported Gnome Versions:

* Gnome Shell 3.2 and higher

Tested Players:

* Amarok
* Banshee - with DBus Mpris plugin
* Clementine
* gmusicbrowser
* Google Music Frame / Nuvola
* Guayadeque
* Quodlibet - with DBus Mpris plugin
* Rhythmbox - with DBus Mpris plugin
* Xnoise

Other Supported Players (may be untested or partially supported):

* Beatbox
* DeaDBeeF
* mpd
* Pithos
* Pragha
* Spotify
* Tomahawk
* xbmc

Note: Audacious is unsupported because it uses an obsolete version of MPRIS. Sorry...

----

### Screenshot
![Screenshot](https://github.com/brianrobles204/Music-Integration/raw/master/data/screenshot.png)

----

### Installation

#### Dependencies

    python
    python-gobject

#### Installation through the Official Gnome website

You can try the extension instantly through the [Gnome Extensions Page](https://extensions.gnome.org/extension/30/music-integration/). <br/>
Unfortunately, installing the extension this way will have the preferences option disabled by default. <br/>
To enable, simply copy-paste the following lines in a terminal, one at a time:

    cd ~/.local/share/gnome-shell/extensions/music-integration@brianrobles204
    sudo cp org.gnome.shell.extensions.musicintegration.gschema.xml /usr/share/glib-2.0/schemas/
    sudo glib-compile-schemas /usr/share/glib-2.0/schemas/

And that's it. Log out and in, or restart the shell for it to take effect.

#### Manual Installation

1. Download and extract.
2. Using a terminal, change your current directory to the extracted folder.
3. Enter the following:

    `# ./autogen.sh`<br />
    `# ./configure --prefix=/usr`<br />
    `# make`<br />
    `# sudo make install`<br />

4. Restart the shell (Alt+F2, enter r, press return) or log out and in.
5. Using Gnome Tweak Tool, enable the extension. `# gnome-tweak-tool`

----

### Authors
Made by [Brian Robles] (mailto:brianrobles204@gmail.com) <br/>
with some help from frandieguez, oxayoti <br/>
This extension is a fork of [Jean-Philippe Braun] (mailto:eon@patapon.info)'s [extension] (https://github.com/eonpatapon/gnome-shell-extensions-mediaplayer)<br/>
