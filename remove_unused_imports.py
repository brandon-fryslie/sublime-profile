import sublime, sublime_plugin, re, os.path

class RemoveUnusedImportsCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		window = sublime.active_window()

		current_file_name = window.active_view().file_name()

		if re.search(controller_re, current_file_name):
			related_file_name = re.sub(controller_re, '.js', current_file_name)
		else:
			related_file_name = re.sub('.js$', 'Controller.js', current_file_name)

		if os.path.isfile(related_file_name):
			window.open_file(related_file_name)