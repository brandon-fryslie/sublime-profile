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

  def find_file_in_ancestors(self, file_name):
    p('find', file_name, 'in ancestors')
    for dirname, dirs, files in self.walk_up(self.get_current_directory()):
      if file_name in files:
        p('found file in ancestor dir', dirname)
        return dirname

  def find_file(self, file_name):

    p('find_file', file_name)

    current_dir = self.get_current_directory()

    file_path = os.path.join(current_dir, file_name)

    p('searching for file', file_path, 'in directory', current_dir)

    p('file_path', os.path.join(current_dir, file_name))

    file_path = os.path.join(self.get_current_directory(), file_name)

    if os.path.isfile(file_path):
      p('found file')
      return file_path

    # Look for possible web dir root
    base_dir = self.find_file_in_ancestors('index.html')
    file_path = os.path.join(base_dir, file_name)

    if os.path.isfile(file_path):
      p('found file in web root')
      return file_path
    else:
      p('find_file did not find', file_path)

  def walk_up(self, bottom):
    """
    mimic os.walk, but walk 'up'
    instead of down the directory tree
    """

    bottom = os.path.realpath(bottom)

    #get files in current dir
    try:
      names = os.listdir(bottom)
    except Exception as e:
      print(e)
      return

    dirs, nondirs = [], []
    for name in names:
      if os.path.isdir(os.path.join(bottom, name)):
        dirs.append(name)
      else:
        nondirs.append(name)

    yield bottom, dirs, nondirs

    new_path = os.path.realpath(os.path.join(bottom, '..'))

    # see if we are at the top
    if new_path == bottom:
      return

    for x in self.walk_up(new_path):
      yield x
