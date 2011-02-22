# line-ending-style.py generated automatically from line-ending-style.py.in
# -*- Mode: Python; coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-
#
# Line Ending Style, a plugin for Gedit (version 2.29.5 or later)
#
# Based in part on the Newline Madness plugin by Jeffery To:
# http://www.thingsthemselves.com/gedit/
#
# Copyright (C) 2010 Daniel Trebbien <dtrebbien@gmail.com>
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

import gedit
import gtk
import gtk.glade

def N_(message): return message

GEDIT_DOCUMENT_NEWLINE_TYPE_LF = 0
GEDIT_DOCUMENT_NEWLINE_TYPE_CR = 1
GEDIT_DOCUMENT_NEWLINE_TYPE_CR_LF = 2

class LineEndingStylePluginUI:
	PLUGIN_MENU_ITEM_PATH_ROOT = "/ui/MenuBar/FileMenu/FileOps_4/LineEndingStylePluginMenu/"

	NOTIFY_NEWLINE_TYPE_HANDLER_ID_KEY = "GeditLineEndingStylePluginUINotifyNewline-TypeHandlerID"

	def __init__(self, window):
		self.window = window

	def merge(self):
		action_group = self.action_group = gtk.ActionGroup("GeditLineEndingStylePluginActions")
		action_group.set_translation_domain("gedit-line-ending-style-plugin")
		action_group.add_actions([
				("LineEndingStylePluginMenu", None, action_group.translate_string(N_("Line Ending Style")), None, None, None) # `translate_string` is called explicitly due to pygtk bug 627656 (https://bugzilla.gnome.org/show_bug.cgi?id=627656)
			])
		action_group.add_radio_actions([
				("LineEndingStylePluginMenuToLFItem", None, action_group.translate_string(N_("Unix/Linux")), None, action_group.translate_string(N_("Switch to Unix/Linux-style line endings (LF)")), GEDIT_DOCUMENT_NEWLINE_TYPE_LF),
				("LineEndingStylePluginMenuToCRItem", None, action_group.translate_string(N_("Mac OS Classic")), None, action_group.translate_string(N_("Switch to Mac OS Classic-style line endings (CR)")), GEDIT_DOCUMENT_NEWLINE_TYPE_CR),
				("LineEndingStylePluginMenuToCRLFItem", None, action_group.translate_string(N_("Windows")), None, action_group.translate_string(N_("Switch to Windows-style line endings (CRLF)")), GEDIT_DOCUMENT_NEWLINE_TYPE_CR_LF)
			], GEDIT_DOCUMENT_NEWLINE_TYPE_LF, lambda action, current: self.set_active_document_newline_type(action.get_current_value()))

		window = self.window
		manager = window.get_ui_manager()
		manager.insert_action_group(action_group, -1)
		self.merge_id = manager.add_ui_from_string("""
			<ui>
				<menubar name="MenuBar">
					<menu name="FileMenu" action="File">
						<placeholder name="FileOps_4">
							<separator />
							<menu name="LineEndingStylePluginMenu" action="LineEndingStylePluginMenu">
								<menuitem name="LineEndingStylePluginMenuToLFItem" action="LineEndingStylePluginMenuToLFItem" />
								<menuitem name="LineEndingStylePluginMenuToCRLFItem" action="LineEndingStylePluginMenuToCRLFItem" />
								<menuitem name="LineEndingStylePluginMenuToCRItem" action="LineEndingStylePluginMenuToCRItem" />
							</menu>
						</placeholder>
					</menu>
				</menubar>
			</ui>
			""")

		statusbar = window.get_statusbar()
		self.sb_frame = gtk.Frame()
		self.sb_label = gtk.Label()
		self.sb_frame.add(self.sb_label)
		statusbar.pack_end(self.sb_frame, False, False)
		self.sb_frame.show_all()

		doc = window.get_active_document()
		if doc:
			self.update_state_per_document(doc)

		self.tab_added_handler_id = window.connect("tab-added", lambda window, tab: self.connect_notify_newline_type_handler(tab.get_document()))
		self.active_tab_changed_handler_id = window.connect("active-tab-changed", lambda window, tab: self.update_state_per_document(tab.get_document()))
		self.tab_removed_handler_id = window.connect("tab-removed", lambda window, tab: self.disconnect_notify_newline_type_handler(tab.get_document()))

		for doc in window.get_documents():
			self.connect_notify_newline_type_handler(doc)

	def connect_notify_newline_type_handler(self, doc):
		notify_newline_type_handler_id = doc.connect("notify::newline-type", lambda doc, pspec: self.update_state_per_document(doc))
		doc.set_data(LineEndingStylePluginUI.NOTIFY_NEWLINE_TYPE_HANDLER_ID_KEY, notify_newline_type_handler_id)

	def disconnect_notify_newline_type_handler(self, doc):
		notify_newline_type_handler_id = doc.get_data(LineEndingStylePluginUI.NOTIFY_NEWLINE_TYPE_HANDLER_ID_KEY)
		doc.set_data(LineEndingStylePluginUI.NOTIFY_NEWLINE_TYPE_HANDLER_ID_KEY, None)
		if notify_newline_type_handler_id != None:
			doc.disconnect(notify_newline_type_handler_id)

	def update_state_per_document(self, doc):
		if doc:
			nl_type = doc.get_property("newline-type")

			next_active_menu_item_name = "LineEndingStylePluginMenuToLFItem"
			next_sb_label_text = self.action_group.translate_string(N_("LF"))
			if nl_type == GEDIT_DOCUMENT_NEWLINE_TYPE_CR:
				next_active_menu_item_name = "LineEndingStylePluginMenuToCRItem"
				next_sb_label_text = self.action_group.translate_string(N_("CR"))
			elif nl_type == GEDIT_DOCUMENT_NEWLINE_TYPE_CR_LF:
				next_active_menu_item_name = "LineEndingStylePluginMenuToCRLFItem"
				next_sb_label_text = self.action_group.translate_string(N_("CRLF"))

			manager = self.window.get_ui_manager()
			manager.get_widget(LineEndingStylePluginUI.PLUGIN_MENU_ITEM_PATH_ROOT + next_active_menu_item_name).set_active(True)
			self.sb_label.set_text(next_sb_label_text)
			self.sb_label.show()
		else:
			self.sb_label.hide()

	def set_active_document_newline_type(self, nl_type):
		doc = self.window.get_active_document()
		if doc:
			doc.set_property("newline-type", nl_type)

	def update_ui(self):
		doc = self.window.get_active_document()
		b = doc != None and not doc.get_readonly()
		manager = self.window.get_ui_manager()
		manager.get_widget(LineEndingStylePluginUI.PLUGIN_MENU_ITEM_PATH_ROOT + "LineEndingStylePluginMenuToLFItem").set_sensitive(b)
		manager.get_widget(LineEndingStylePluginUI.PLUGIN_MENU_ITEM_PATH_ROOT + "LineEndingStylePluginMenuToCRItem").set_sensitive(b)
		manager.get_widget(LineEndingStylePluginUI.PLUGIN_MENU_ITEM_PATH_ROOT + "LineEndingStylePluginMenuToCRLFItem").set_sensitive(b)
		self.update_state_per_document(doc)

	def unmerge(self):
		window = self.window
		for doc in window.get_documents():
			self.disconnect_notify_newline_type_handler(doc)
		window.disconnect(self.tab_removed_handler_id); del self.tab_removed_handler_id
		window.disconnect(self.active_tab_changed_handler_id); del self.active_tab_changed_handler_id
		window.disconnect(self.tab_added_handler_id); del self.tab_added_handler_id
		gtk.HBox.remove(window.get_statusbar(), self.sb_frame); del self.sb_frame
		manager = window.get_ui_manager()
		manager.remove_ui(self.merge_id); del self.merge_id
		manager.remove_action_group(self.action_group); del self.action_group
		manager.ensure_update()
		del self.window

class LineEndingStylePlugin(gedit.Plugin):
	UI_KEY = "GeditLineEndingStylePluginUI"

	def __init__(self):
		gedit.Plugin.__init__(self)

	def activate(self, window):
		ui = LineEndingStylePluginUI(window)
		ui.merge()
		window.set_data(LineEndingStylePlugin.UI_KEY, ui)

	def deactivate(self, window):
		ui = window.get_data(LineEndingStylePlugin.UI_KEY)
		window.set_data(LineEndingStylePlugin.UI_KEY, None)
		ui.unmerge()

	def update_ui(self, window):
		ui = window.get_data(LineEndingStylePlugin.UI_KEY)
		ui.update_ui()

gtk.glade.bindtextdomain("gedit-line-ending-style-plugin", "/usr/share/locale")
