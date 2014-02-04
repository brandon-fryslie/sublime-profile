import sublime, sublime_plugin, re, os.path

window = sublime.active_window()


class GotoSuperclassMethodCommand(sublime_plugin.TextCommand):

    def get_superclass_name(self):
        view = self.view
        extend_re = r'extend:\s+[\'"]((Rally|Ext)(\.|\w+)+).*'
        extend_region = view.find(extend_re, 0)
        s = view.substr(extend_region)
        matches = re.match(extend_re, s)
        if matches:
            return matches.group(1)
        else:
            raise Exception("Cannot find superclass name")


    def get_path_for_filename(self, file_name):
        if re.match('^Rally', file_name):
            base_path = os.path.expanduser('~/projects/appsdk/rui/src/')
        else:
            base_path = os.path.expanduser('~/projects/appsdk/lib/ext/4.2.2/src/')

        file_name = re.sub('^(Rally|Ext).', '', file_name)

        file_name = re.sub('\.', '/', file_name) + '.js'

        return os.path.join(base_path, file_name)

    def open_window_for_file(self, file_name):

        if os.path.isfile(file_name):

            print('trying to open file', file_name)

            window.open_file(file_name)

        else:

            print('could not find file', file_name)




    def run(self, edit):
        window = sublime.active_window()
        view = self.view

        superclass_name = self.get_superclass_name()

        superclass_path = self.get_path_for_filename(superclass_name)

        self.open_window_for_file(superclass_path)

        # for region in view.sel():



            # find current method name
            # find superclass name
            # navigate up hierarchy until superclass implementing method is found
            # navigate to method in superclass

            # extend_region = self.view.find(r'extend: ['"](Rally|Ext)\.')

            # file_to_open = view.substr(view.extract_scope(region.begin())).strip('\'"')

            # file_to_open = re.sub('^Rally.', '', file_to_open)

            # file_to_open = re.sub('\.', '/', file_to_open) + '.js'

            # file_to_open = base_path + file_to_open

            # if os.path.isfile(file_to_open):

            #     window.open_file(file_to_open)

            # else:

            #     print('could not find file', file_to_open)