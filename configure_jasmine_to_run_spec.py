import sublime, sublime_plugin, re, os.path, subprocess

def run_command(args):
    TEST = 1

    if TEST:
        print('=>', ' '.join(args))
        return ('<result>', '<err>', 0)
    else:
        startupinfo = None
        if os.name == 'nt':
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        proc = subprocess.Popen(args, stdout=subprocess.PIPE,
                                startupinfo=startupinfo, stderr=subprocess.PIPE)

        (result, err) = proc.communicate()

        return (result, err, proc.returncode)

class ConfigureJasmineToRunSpecCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        window = sublime.active_window()

        (file_name, ext) = os.path.splitext(self.view.file_name())

        os.chdir(os.path.expanduser('~/projects/appsdk'))

        file_name = os.path.basename(file_name)

        (result, err, _) = run_command(['grunt', 'test:fastconf', '--jsspec=' + file_name])

        print(result)
        print(err)