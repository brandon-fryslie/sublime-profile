import sublime, sublime_plugin, re, os.path

class GotoSuperclassMethodCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        window = sublime.active_window()
        view = self.view

        base_path = os.path.expanduser('~/projects/appsdk/rui/src/')

        for region in view.sel():

            # find current method name
            # find superclass name
            # navigate up hierarchy until superclass implementing method is found
            # navigate to method in superclass


            extend_region = self.view.find(r'extend: ['"](Rally|Ext)\.')



            file_to_open = view.substr(view.extract_scope(region.begin())).strip('\'"')

            file_to_open = re.sub('^Rally.', '', file_to_open)

            file_to_open = re.sub('\.', '/', file_to_open) + '.js'

            file_to_open = base_path + file_to_open

            if os.path.isfile(file_to_open):

                window.open_file(file_to_open)

            else:
                
                print('could not find file', file_to_open)