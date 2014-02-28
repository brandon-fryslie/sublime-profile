import os

DEBUG=1

def p(*args):
  global DEBUG
  if DEBUG:
    print(*args)

class Toolbox:
  def __init__(self, view):
    self.view = view
    self.region = view.sel()[0]

  def scope_matches(self, scope):

    return self.view.score_selector(self.region.begin(), scope)

  def get_scope_content(self):
    return self.view.substr(self.view.extract_scope(self.region.begin()))

  def get_current_directory(self):
    return os.path.dirname(self.view.file_name())

  def find_file(self, file_name):

    p('find_file', file_name)

    file_path = os.path.join(self.get_current_directory(), file_name)

    # p('searching for file', file_path)

    if os.path.isfile(file_path):
      p('found file')
      return file_path
    else:
      p('find_file did not find', file_path)