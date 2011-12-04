## Music Integration Extension
Integrate your music with the Gnome Shell.

This extension listens to Dbus MPRIS and automatically looks for players. It then adds an icon to the 
Gnome panel when it finds a music player and creates a nice notification when the song changes.
You also have an option to integrate the player into the volume menu, much like in Ubuntu's setup.
All these options are configurable through a nice GUI tool.


### Screenshot
![Screenshot](https://github.com/brianrobles204/Music-Integration/raw/master/screenshot.png)


### Installation
You can try the extension instantly through the Gnome Extensions Page 
- https://extensions.gnome.org/extension/30/music-integration/
Unfortunately, installing the extension this way will have the preferences option disabled by default.
To enable, simply copy-paste the following in a terminal:

* `cd ~/.local/share/gnome-shell/extensions/music-integration@brianrobles204`
* `sudo cp org.gnome.shell.extensions.musicintegration.gschema.xml /usr/share/glib-2.0/schemas/`
* `sudo glib-compile-schemas /usr/share/glib-2.0/schemas/`

And that's it. Log out and in, or restart the shell for it to take effect.


If you choose to install it manually, use the following instructions:

1. Download and extract.
2. Put the folder `music-integration@brianrobles204` in `~/.local/share/gnome-shell/extensions/`
3. As root, put `org.gnome.shell.extensions.musicintegration.gschema.xml` in `/usr/share/glib-2.0/schemas/`
4. As root, in terminal, run: `# glib-compile-schemas /usr/share/glib-2.0/schemas/`
5. Restart the shell (Alt+F2, enter r, press enter) or log out and in.
6. Using Gnome Tweak Tool, enable the extension. `# gnome-tweak-tool`


### Authors
Made by Brian Robles (brianrobles204@gmail.com) <br/>
This extension is a fork of Jean-Philippe Braun's extension (eon@patapon.info)<br/>
Original: https://github.com/eonpatapon/gnome-shell-extensions-mediaplayer<br/>
