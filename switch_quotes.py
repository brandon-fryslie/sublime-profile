import sublime, sublime_plugin, re, os.path

# TODO:
# make this work for strings like this: "'" '"'
# make this work for strings like this: r"blablabla"

class SwitchQuotesCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        window = sublime.active_window()
        view = self.view

        for region in view.sel():

            syntax = self.view.scope_name(region.begin())

            if re.search(r"(parameter\.url|string\.quoted\.(double|single))", syntax):

                string_region = view.extract_scope(region.begin())

                string_string = view.substr(string_region)

                new_quote_type = "'" if string_string[0] ==  '"' else '"'

                s = view.substr(string_region).strip('\'"')

                new_s = new_quote_type + s + new_quote_type

                self.view.replace(edit, string_region, new_s)
