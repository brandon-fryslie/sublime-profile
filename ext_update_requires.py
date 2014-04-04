import sublime, sublime_plugin, re, os.path

import User.toolbox
from User.toolbox import Toolbox, p

def sorted_uniq_list(l):
  return sorted(list(set(l)))

def indent_by(n):
  tab_size = 4
  return  ' ' * n * tab_size

def create_requires_list(l):
  indent_level = 2
  last_index = len(l) - 1
  str = 'requires: [\n'
  for i, classname in enumerate(l):
    str += indent_by(indent_level + 1) + "'{0}'".format(classname)
    if i != last_index:
      str += ','
    str += '\n'
  return str + indent_by(indent_level) + ']'



class ExtUpdateRequiresCommand(sublime_plugin.TextCommand):

  # TODO:
  # figure out aliases
  # figure out xtypes
  # match indent level for requires list
  # exclude usages found in comments
  # make this work if file does not already have a requires block
  # should we exclude ext core classes?

  def run(self, edit):

    view = self.view

    # get list of all requires
    requires_region = view.find('requires:\s*\[[^\]]*\]', 0)
    # requires = view.substr(requires_region)

    # match Ext classnames
    ext_class_re_str = '((?:Ext|Rally)(?:\.\w+)*(?:\.[A-Z]\w+))'
    ext_class_re = re.compile(ext_class_re_str)

    # requires = sorted_uniq_list(ext_class_re.findall(requires))

    # get regions of all ext class usages
    usage_regions = view.find_all(ext_class_re_str)

    # exclude usages in comments
    def not_in_comment(region):
      return view.score_selector(region.a, 'comment') == 0

    usage_regions = filter(not_in_comment, usage_regions)

    usages = sorted_uniq_list([view.substr(region) for region in usage_regions])

    # # exclude current class and Ext.define
    current_class_name = view.substr(view.find('Ext.define.*'+ext_class_re_str, 0))
    current_class_name = ext_class_re.search(current_class_name).group(0)

    blacklist = ['Ext.define', current_class_name]

    # # remove items we don't need to import
    usages = [x for x in usages if x not in blacklist]

    # # all import usages - all requires = all usages not in a requires
    # unrequired_usages = [x for x in usages if x not in requires]

    # # Simply write out new requires list with all usages
    new_requires_list = create_requires_list(usages)

    print(new_requires_list)

    view.replace(edit, requires_region, new_requires_list)