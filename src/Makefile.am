AM_CPPFLAGS = -DLOCALEDIR=\"$(localedir)\"
LDADD = $(LIBINTL)

EXTRA_DIST = lineendingstyle.plugin lineendingstyle.py \
	lineendingstyle.py.in

plugin_DATA = lineendingstyle.plugin lineendingstyle.py

lineendingstyle.py: lineendingstyle.py.in Makefile
	echo '# $(@) generated automatically from $(<)' >$@
	$(SED) "s/@""localedir@/$(shell echo $(localedir)| $(SED) -e 's/\\/\\\\/g' -e 's/\"/\\\"/g' -e 's/\\/\\\\/g' -e 's/\//\\\//g' -e 's/&/\\\&/g')/g" <$< >>$@
