import sublime, sublime_plugin

class ExtendHeadingCommand(sublime_plugin.TextCommand):
	def insertTab(self, edit, view, position):

		view.insert(edit, cursor_position, '\t')

		return

	def getCurrentLine(self, view, region):
		return view.line(region)

	def run(self, edit):

		if len(self.view.sel()) > 1:

			[self.insertTab(edit, view, region.begin()) for region in self.view.sel()]

			return

		region = self.view.sel()[0]
		cursor_position = region.begin()

		current_line = self.getCurrentLine(self.view, region)
		
		line_number, col_number = self.view.rowcol(cursor_position)

		if col_number > 2 or line_number < 1:
			return

		previous_char = self.view.substr(sublime.Region(cursor_position - 1, cursor_position))

		if previous_char != '=' and previous_char != '-':
			return

		offset = self.view.text_point(line_number - 1, 0)

		previous_line = self.view.substr(self.view.line(offset))

		previous_line_length = len(previous_line.strip())

		current_line_length = len(self.view.substr(current_line).strip())

		self.view.replace(edit, sublime.Region(cursor_position, cursor_position + current_line_length), previous_char * (previous_line_length - 1) + '\n')

	# def onQueryContext(view, key, value):
	# 	print('on query context')
	# 	print(key)
