import sublime, sublime_plugin, re, os.path

import User.toolbox
from User.toolbox import Toolbox, p

import imp
imp.reload(User.toolbox)

p('Debug is on')

class GotoLinkInHtmlCommand(sublime_plugin.TextCommand):

  def open_window_for_file(self, file_name):
    window = sublime.active_window()

    if os.path.isfile(file_name):

      p('trying to open file', file_name)

      window.open_file(file_name)

    else:

      p('could not find file', file_name)

  def run(self, edit):
    self.toolbox = Toolbox(self.view)

    file_name = self.toolbox.get_scope_content()

    file_name = self.toolbox.find_file(file_name.strip('\'\'""'))

    if file_name is None:
      p('countnt find a file! make find better')
      return

    p('file_name', file_name)

    self.open_window_for_file(file_name)