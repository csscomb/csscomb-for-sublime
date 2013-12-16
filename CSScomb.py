# coding: utf-8

import sys
import sublime
import sublime_plugin
import subprocess
import json
from os import path, name

__file__ = path.normpath(path.abspath(__file__))
__path__ = path.dirname(__file__)
libs_path = path.join(__path__, 'libs')
csscomb_path = path.join(libs_path, 'call_string.php')
is_python3 = sys.version_info[0] > 2


def to_unicode_or_bust(obj, encoding='utf-8'):
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj = unicode(obj, encoding)
    return obj


class CssSorter(sublime_plugin.TextCommand):

    def __init__(self, view):
        self.view = view
        self.startupinfo = None
        self.error = False
        if name == 'nt':
            self.startupinfo = subprocess.STARTUPINFO()
            self.startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            self.startupinfo.wShowWindow = subprocess.SW_HIDE

    def run(self, edit):
        self.check_php_on_path()

        self.sortorder = False
        self.order_settings = sublime.load_settings('CSScomb.sublime-settings')
        if self.order_settings.has('custom_sort_order') and self.order_settings.get('custom_sort_order') is True:
            self.sortorder = json.dumps(self.order_settings.get('sort_order'))
            sublime.status_message('Sorting with custom sort order...')
        else:
            self.sortorder = ''

        selections = self.get_selections()

        for sel in selections:
            selbody = self.view.substr(sel)

            if is_python3:
                selbody = str(selbody)
            else:
                selbody = selbody.encode('utf-8')

            myprocess = subprocess.Popen(['php', csscomb_path, selbody, self.sortorder], shell=False, stdout=subprocess.PIPE, startupinfo=self.startupinfo)
            (sout, serr) = myprocess.communicate()
            myprocess.wait()

            if serr:
                sublime.error_message(self.status)
                return
            elif sout is None:
                sublime.error_message('There was an error sorting CSS.')
                return

            if is_python3:
                result = str(sout, encoding='utf-8')
            else:
                result = to_unicode_or_bust(sout)

            self.view.replace(edit, sel, result)

        sublime.status_message('Successfully sorted')

    def get_selections(self):
        selections = self.view.sel()

        # check if the user has any actual selections
        has_selections = False
        for region in selections:
            if region.empty() is False:
                has_selections = True

        # if not, add the entire file as a selection
        if not has_selections:
            full_region = sublime.Region(0, self.view.size())
            selections.add(full_region)

        return selections

    def check_php_on_path(self):
        try:
            subprocess.call(['php', '-v'], shell=False, startupinfo=self.startupinfo)
        except (OSError):
            sublime.error_message('Plugin unable to find php on computer.\nCSScomb needs PHP to function properly.\n\nPlease make sure you have installed PHP\nand it is available in your PATH:\n\nhttp://php.net/downloads.php')
            return
