import sublime, sublime_plugin, re, os.path

class OpenExtFileCommand(sublime_plugin.TextCommand):

  def run(self, edit):
    window = sublime.active_window()
    view = self.view

    for region in view.sel():

      syntax = self.view.scope_name(region.begin())

      if re.search(r"(parameter\.url|string\.quoted\.(double|single))", syntax):

        file_to_open = view.substr(view.extract_scope(region.begin())).strip('\'"')

        if re.match('^Rally', file_to_open):
          base_path = os.path.expanduser('~/projects/appsdk/rui/src')
        else:
          base_path = os.path.expanduser('~/projects/appsdk/lib/ext/4.2.2/src')

        file_to_open = re.sub('^(Rally|Ext).', '', file_to_open)

        file_to_open = re.sub('\.', '/', file_to_open) + '.js'

        file_to_open = os.path.join(base_path, file_to_open)

        if os.path.isfile(file_to_open):

          window.open_file(file_to_open)

        else:

          print('could not find file', file_to_open)