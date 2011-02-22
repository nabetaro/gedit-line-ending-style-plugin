AM_CPPFLAGS = -DLOCALEDIR=\"$(localedir)\"
LDADD = $(LIBINTL)

EXTRA_DIST = line-ending-style.gedit-plugin line-ending-style.py \
	line-ending-style.py.in

plugin_DATA = line-ending-style.gedit-plugin line-ending-style.py

line-ending-style.py: line-ending-style.py.in Makefile
	echo '# $(@) generated automatically from $(<)' >$@
	$(SED) "s/@""localedir@/$(shell echo $(localedir)| $(SED) -e 's/\\/\\\\/g' -e 's/\"/\\\"/g' -e 's/\\/\\\\/g' -e 's/\//\\\//g' -e 's/&/\\\&/g')/g" <$< >>$@
