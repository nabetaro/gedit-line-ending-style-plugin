## Introduction
This is a plugin for Gedit 3 that allows the line ending style of documents to be quickly ascertained and changed. It adds a small, dual-purpose combo box to the status bar which indicates the current document's line ending style and allows it to be changed.

## Local installation
Local installation of the plugin is for when you don't have root access or you only want to install it for yourself.

 0. You may need to create some directories if you haven't installed Gedit plugins locally before:

    <pre>
mkdir --parents ~/.local/share/gedit/plugins
</pre>
 1. Save the latest [`lineendingstyle.plugin`](https://github.com/dtrebbien/gedit-line-ending-style-plugin/raw/master/src/lineendingstyle.plugin) and [`lineendingstyle.py`](https://github.com/dtrebbien/gedit-line-ending-style-plugin/raw/master/src/lineendingstyle.py) to `~/.local/share/gedit/plugins`
 2. Re-start Gedit.
 3. From the Edit menu, select "Preferences".
 4. On the Plugins tab, scroll down to the entry for "Line Ending Style" and check the checkbox.
 5. Click Close.

### Uninstallation
 0. From the Edit menu, select "Preferences".
 1. On the Plugins tab, scroll down to the entry for "Line Ending Style" and uncheck the checkbox.
 2. Close Gedit.
 3. Delete `lineendingstyle.plugin` and `lineendingstyle.py` from `~/.local/share/gedit/plugins`.

## Notes
 *  It is not currently possible to undo changing the line ending style.
 *  If the current document is read-only, the line ending style combo box is disabled.
 *  The plugin was originally inspired by [Jeffery To](https://github.com/jefferyto)'s Newline Madness plugin for Gedit 2.

## License
<pre>
Copyright © 2012  Daniel Trebbien

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
</pre>
