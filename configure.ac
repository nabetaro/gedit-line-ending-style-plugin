AC_INIT([Gedit Line Ending Style plugin], [0.1], [dtrebbien@gmail.com], [gedit-line-ending-style-plugin], [http://code.google.com/p/gedit-line-ending-style-plugin/])
AC_CONFIG_MACRO_DIR([m4])
AM_INIT_AUTOMAKE([1.10 no-define foreign dist-bzip2])

dnl plugindir=${libdir}/gedit-2/plugins
dnl AC_DEFINE_DIR(PLUGINDIR, [plugindir], [Gedit plugin files])

dnl AS_AC_EXPAND(PLUGINDIR, ${libdir}/gedit-2/plugins)
dnl AC_DEFINE_UNQUOTED(PLUGINDIR, "${PLUGINDIR}", [Gedit plugin files])
dnl plugindir="\$(libdir)/gedit-2/plugins"
dnl AC_SUBST(plugindir)
dnl AC_MSG_NOTICE([Using $PLUGINDIR as the installation directory for Gedit plugin files])
AC_SUBST([plugindir], ['${libdir}/gedit-2/plugins'])

AM_GNU_GETTEXT_VERSION(0.18.1)
AM_GNU_GETTEXT([external])

AC_CONFIG_FILES([
Makefile
po/Makefile.in
src/Makefile
])

AC_OUTPUT
