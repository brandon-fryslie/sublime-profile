import sublime, sublime_plugin, re, os.path

# TODO:
# make this work for strings like this: "'" '"' """""", etc
# make this work for strings like this: r"blablabla"


class SwitchQuotesCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        window = sublime.active_window()
        view = self.view

        for region in view.sel():

            syntax = self.view.scope_name(region.begin())

            syntax_pattern = re.compile(r"(?:parameter\.url|string\.quoted\.(?:double|single)((\.block)?))")

            matches = re.search(syntax_pattern, syntax)

            if matches:

                if matches.group(1):
                    QUOTE_MULTIPLIER = 3
                else:
                    QUOTE_MULTIPLIER = 1

                string_region = view.extract_scope(region.begin())

                string_string = view.substr(string_region)

                new_quote_type = "'" if string_string[-1] ==  '"' else '"'

                s = re.sub(r'^(r?)(?:("|\')+)', r'\1' + (new_quote_type * QUOTE_MULTIPLIER), string_string)

                s = s.rstrip('\'"')

                new_s =  s + new_quote_type * QUOTE_MULTIPLIER

                self.view.replace(edit, string_region, new_s)
