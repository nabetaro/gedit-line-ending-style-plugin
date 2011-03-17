# line-ending-style.py generated automatically from line-ending-style.py.in
# -*- Mode: Python; coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-
#
# Line Ending Style, a plugin for Gedit (version 2.29.5 or later)
#
# Based in part on the Newline Madness plugin by Jeffery To:
# http://www.thingsthemselves.com/gedit/
#
# Copyright © 2011 Daniel Trebbien <dtrebbien@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gettext
from gi.repository import GObject, Gtk, Gedit, Peas, PeasGtk

class LineEndingStylePluginUi:
	ITEM_VALUE_KEY = "GeditLineEndingStylePluginUiItemValue"
	NOTIFY_NEWLINE_TYPE_HANDLER_ID_KEY = "GeditLineEndingStylePluginUiNotifyNewline-TypeHandlerId"

	def __init__(self, window):
		self.window = window

	def merge(self):
		action_group = self.action_group = Gtk.ActionGroup("GeditLineEndingStylePluginActions")
		action_group.set_translation_domain("gedit-line-ending-style-plugin")
		_ = lambda string: action_group.translate_string(string)

		window = self.window
		statusbar = window.get_statusbar()
		sb_combo = self.sb_combo = Gedit.StatusComboBox.new(None)

		entries = [
					("LineEndingStylePluginStatusComboToLFItem", "Unix/Linux", "Switch to Unix/Linux-style line endings (LF)",
							Gedit.DocumentNewlineType.LF, "LF"),
					("LineEndingStylePluginStatusComboToCRItem", "Mac OS Classic", "Switch to Mac OS Classic-style line endings (CR)",
							Gedit.DocumentNewlineType.CR, "CR"),
					("LineEndingStylePluginStatusComboToCRLFItem", "Windows", "Switch to Windows-style line endings (CRLF)",
							Gedit.DocumentNewlineType.CR_LF, "CRLF")
				]
		activate_callback = lambda item: self.set_active_document_newline_type(item.get_data(LineEndingStylePluginUi.ITEM_VALUE_KEY))
		for entry in entries:
			action = Gtk.Action(entry[0],
					_(entry[1]),
					_(entry[2]),
					None)
			action_group.add_action(action)
			item = action.create_menu_item()
			item.set_data(LineEndingStylePluginUi.ITEM_VALUE_KEY, entry[3])
			item.connect("activate", activate_callback)
			sb_combo.add_item(item, _(entry[4]))

		sb_combo.show_all()
		statusbar.pack_end(sb_combo, False, True, 0)

		doc = window.get_active_document()
		if doc:
			self.update_state_per_document(doc)

		self.tab_added_handler_id = window.connect("tab-added",
				lambda window, tab: self.connect_notify_newline_type_handler(tab.get_document()))
		self.active_tab_changed_handler_id = window.connect("active-tab-changed",
				lambda window, tab: self.update_state_per_document(tab.get_document()))
		self.tab_removed_handler_id = window.connect("tab-removed",
				lambda window, tab: self.disconnect_notify_newline_type_handler(tab.get_document()))

		for doc in window.get_documents():
			self.connect_notify_newline_type_handler(doc)

	def connect_notify_newline_type_handler(self, doc):
		notify_newline_type_handler_id = doc.connect("notify::newline-type", lambda doc, pspec: self.update_state_per_document(doc))
		doc.set_data(LineEndingStylePluginUi.NOTIFY_NEWLINE_TYPE_HANDLER_ID_KEY, notify_newline_type_handler_id)

	def disconnect_notify_newline_type_handler(self, doc):
		notify_newline_type_handler_id = doc.get_data(LineEndingStylePluginUi.NOTIFY_NEWLINE_TYPE_HANDLER_ID_KEY)
		doc.set_data(LineEndingStylePluginUi.NOTIFY_NEWLINE_TYPE_HANDLER_ID_KEY, None)
		if notify_newline_type_handler_id != None:
			doc.disconnect(notify_newline_type_handler_id)

	def update_state_per_document(self, doc):
		sb_combo = self.sb_combo

		if doc:
			nl_type = doc.get_property("newline-type")

			for item in sb_combo.get_items():
				if item.get_data(LineEndingStylePluginUi.ITEM_VALUE_KEY) == nl_type:
					sb_combo.set_item(item)
					break

			sb_combo.show()
		else:
			sb_combo.hide()

	def set_active_document_newline_type(self, nl_type):
		doc = self.window.get_active_document()
		if doc:
			doc.set_property("newline-type", nl_type)

	def update_ui(self):
		doc = self.window.get_active_document()
		if doc:
			b = not doc.get_readonly()
			self.sb_combo.set_sensitive(b)
		self.update_state_per_document(doc)

	def unmerge(self):
		window = self.window
		for doc in window.get_documents():
			self.disconnect_notify_newline_type_handler(doc)
		window.disconnect(self.tab_removed_handler_id); del self.tab_removed_handler_id
		window.disconnect(self.active_tab_changed_handler_id); del self.active_tab_changed_handler_id
		window.disconnect(self.tab_added_handler_id); del self.tab_added_handler_id
		Gtk.HBox.remove(window.get_statusbar(), self.sb_combo); del self.sb_combo
		del self.window

class LineEndingStylePlugin(GObject.Object, Gedit.WindowActivatable):
	__gtype_name__ = "LineEndingStylePlugin"

	UI_KEY = "GeditLineEndingStylePluginUi"

	window = GObject.property(type = Gedit.Window)

	def __init__(self):
		pass

	def do_activate(self):
		window = self.window
		ui = LineEndingStylePluginUi(window)
		ui.merge()
		window.set_data(LineEndingStylePlugin.UI_KEY, ui)
		pass

	def do_deactivate(self):
		window = self.window
		ui = window.get_data(LineEndingStylePlugin.UI_KEY)
		window.set_data(LineEndingStylePlugin.UI_KEY, None)
		ui.unmerge()
		pass

	def do_update_state(self):
		window = self.window
		ui = window.get_data(LineEndingStylePlugin.UI_KEY)
		ui.update_ui()
		pass

gettext.bindtextdomain("gedit-line-ending-style-plugin", "/usr/share/locale")
