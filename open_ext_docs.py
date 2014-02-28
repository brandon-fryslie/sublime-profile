import sublime, sublime_plugin, re, os.path, webbrowser

class OpenExtDocCommand(sublime_plugin.TextCommand):

  def run(self, edit):
    window = sublime.active_window()
    view = self.view

    base_doc_url = 'http://localhost:7001/slm/js-lib/rui/builds/doc/#!/api/'

    for region in view.sel():

      syntax = self.view.scope_name(region.begin())

      if re.search(r"(parameter\.url|string\.quoted\.(double|single))", syntax):

        ext_object = view.substr(view.extract_scope(region.begin())).strip('\'"')

        url_to_open = base_doc_url + ext_object

        is_ext_object_re = re.compile('(?!(?!Ext|Rally)(?!\.\w+)+)')
        if is_ext_object_re.search(ext_object):

          webbrowser.open_new_tab(url_to_open)

        else:

          print('not valid ext object: ', ext_object)