AM_CPPFLAGS = -DLOCALEDIR=\"$(localedir)\"
LDADD = $(LIBINTL)

EXTRA_DIST = lineendingstyle.plugin lineendingstyle.plugin.in \
	lineendingstyle.py lineendingstyle.py.in

plugin_DATA = lineendingstyle.plugin lineendingstyle.py

lineendingstyle.py: lineendingstyle.py.in Makefile
	echo '# -*- mode: Text; coding: utf-8; buffer-read-only: t -*-' >$@
	echo '# $(@) generated automatically from $(<)' >>$@
	$(SED) -e '1d' -e "s/@""localedir@/$(shell echo $(localedir)| $(SED) -e 's/\\/\\\\/g' -e 's/\"/\\\"/g' -e 's/\\/\\\\/g' -e 's/\//\\\//g' -e 's/&/\\\&/g')/g" <$< >>$@
