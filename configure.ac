AC_INIT([Gedit Line Ending Style plugin], [0.1.1a], [dtrebbien@gmail.com], [gedit-line-ending-style-plugin], [https://github.com/dtrebbien/gedit-line-ending-style-plugin/])
AC_CONFIG_MACRO_DIR([m4])
AM_INIT_AUTOMAKE([1.10 no-define foreign dist-bzip2])

AC_SUBST([plugindir], ['${libdir}/gedit/plugins'])

AC_PROG_SED

AM_GNU_GETTEXT_VERSION(0.17)
AM_GNU_GETTEXT([external])

AC_CONFIG_FILES([
Makefile
po/Makefile.in
src/lineendingstyle.plugin
src/Makefile
])

AC_OUTPUT
