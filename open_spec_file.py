import sublime, sublime_plugin, re, os.path

class OpenSpecFileCommand(sublime_plugin.TextCommand):

    def get_spec_path(self, file_name):
        file_name = re.sub('rui/src', 'rui/test/coffeescripts/rui', file_name)
        return os.path.join(file_name + 'Spec' + '.coffee')

    def get_test_path(self, file_name):
        file_name = re.sub('rui/src', 'rui/test/legacy/rui', file_name)
        return os.path.join(file_name + 'Test' + '.js')

    def open_spec_file(self, file_name):
        if os.path.isfile(self.get_spec_path(file_name)):
            sublime.active_window().open_file(self.get_spec_path(file_name))
        elif os.path.isfile(self.get_test_path(file_name)):
            sublime.active_window().open_file(self.get_test_path(file_name))
        else:
            print('could not find test file at', self.get_spec_path(file_name), 'or', self.get_test_path(file_name))

    def get_component_path(self, file_name):
        file_name = re.sub('(rui/test/legacy/rui|rui/test/coffeescripts/rui)', 'rui/src', file_name)
        return re.sub('(Spec|Test)$', '.js', file_name) 


    def open_component_for_spec_file(self, file_name):
        file_to_open = self.get_component_path(file_name)
        if os.path.isfile(file_to_open):
            sublime.active_window().open_file(file_to_open)
        else:
            print('could not find component file', file_to_open)

    def run(self, edit):
        window = sublime.active_window()

        (file_name, ext) = os.path.splitext(self.view.file_name())

        if re.search('(Spec|Test)$', file_name):
            self.open_component_for_spec_file(file_name)
        else:
            self.open_spec_file(file_name)
