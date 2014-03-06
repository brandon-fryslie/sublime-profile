import sublime, sublime_plugin, re, os

import User.toolbox
from User.toolbox import Toolbox, p

import imp
imp.reload(User.toolbox)

p('Debug is on')

class GotoLinkInHtmlCommand(sublime_plugin.TextCommand):

  # file_path - Takes a full file path
  def open_window_for_file(self, file_path):
    window = sublime.active_window()

    # path = os.path.join(self.toolbox.get_current_directory(), file_path)

    if os.path.isfile(file_path):

      p('trying to open file', file_path)

      window.open_file(file_path)

    else:

      p('could not find file', file_path)

  def run(self, edit):
    self.toolbox = Toolbox(self.view)

    current_dir = self.toolbox.get_current_directory()

    file_name = self.toolbox.get_scope_content()

    file_name = file_name.strip('\'\'""/')

    file_name = self.toolbox.find_file(file_name.strip('\'\'""/'))

    if re.search(".js$", file_name):
      coffee_file = file_name.rstrip(".js") + '.coffee'
      if os.path.isfile(coffee_file):
        file_name = coffee_file

    if file_name is None:
      p('countnt find a file! make find better')
      return

    p('file_name', file_name)

    self.open_window_for_file(file_name)