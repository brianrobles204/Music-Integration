# Change these to modify how installation is performed
extensionurl = https://github.com/brianrobles204/Music-Integration
topextensiondir = $(datadir)/gnome-shell/extensions
extensiondir = $(topextensiondir)/$(uuid)
uuid = music-integration@brianrobles204

nobase_dist_extension_DATA = extension.js stylesheet.css icons Makefile.am music-int-pref.py music.png pause.png play.png
nodist_extension_DATA = metadata.json $(EXTRA_EXTENSION)

EXTRA_DIST = metadata.json.in
CLEANFILES = metadata.json

gschemas_in = org.gnome.shell.extensions.musicintegration.gschema.xml.in

@INTLTOOL_XML_NOMERGE_RULE@

gsettings_SCHEMAS = $(gschemas_in:.xml.in=.xml)

@GSETTINGS_RULES@

CLEANFILES += $(gschemas_in:.xml.in=.valid) $(gsettings_SCHEMAS)
EXTRA_DIST += $(gschemas_in)

metadata.json: metadata.json.in $(top_builddir)/config.status
	$(AM_V_GEN) sed -e "s|[@]LOCALEDIR@|$(datadir)/locale|" \
	    -e "s|[@]EXTENSIONDIR@|$(extensiondir)|" \
	    -e "s|[@]UUID@|$(uuid)|" \
	    -e "s|[@]URL@|$(extensionurl)|" $< > $@

