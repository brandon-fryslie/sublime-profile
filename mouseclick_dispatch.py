import sublime, sublime_plugin, re, os.path, sys

from User.toolbox import Toolbox, p

class MouseclickDispatchCommand(sublime_plugin.TextCommand):

  def run_command(self, command, is_window_scope):
    p('running command', command)
    if is_window_scope:
      window = sublime.active_window()
      window.run_command(command)
    else:
      self.view.run_command(command)

  def run(self, edit):
    self.toolbox = Toolbox(self.view)

    mousemap = [
      {
        'context': {
          'scope': 'string.quoted.double.html'
        },
        'command': 'goto_link_in_html'
      },
      {
        'context': {
          'scope': 'source.coffee string, source.js string'
        },
        'command': 'open_ext_file'
      },
      {
        'context': {
          'scope': ''
        },
        'command': 'goto_definition',
        'window_scope': True
      }
    ]

    for m in mousemap:

      context = m['context']

      if self.toolbox.scope_matches(context['scope']):
        self.run_command(m['command'], 'window_scope' in m)
        return

    p('couldnt match anything')