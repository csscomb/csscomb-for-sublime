# coding: utf-8

import sublime
import sublime_plugin
from csscomb import LocalSort


def to_unicode_or_bust(obj, encoding='utf-8'):
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj = unicode(obj, encoding)
    return obj


class BaseSorter(sublime_plugin.TextCommand):
    """Base Sorter"""

    def __init__(self, view):
        self.view = view

    def run(self, edit):

        selections = self.get_selections()

        threads = []
        for sel in selections:
            selbody = self.view.substr(sel)
            selbody = selbody.encode('utf-8')
            thread = LocalSort(sel, selbody)

            threads.append(thread)
            thread.start()

        self.handle_threads(edit, threads, selections, offset=0, i=0)

    def get_selections(self):
        selections = self.view.sel()

        # check if the user has any actual selections
        has_selections = False
        for sel in selections:
            if sel.empty() == False:
                has_selections = True

        # if not, add the entire file as a selection
        if not has_selections:
            full_region = sublime.Region(0, self.view.size())
            selections.add(full_region)

        return selections

    def handle_threads(self, edit, threads, selections, offset=0, i=0):

        next_threads = []
        for thread in threads:
            if thread.is_alive():
                next_threads.append(thread)
                continue
            if thread.result == False:
                continue
            self.handle_result(edit, thread, selections, offset)
        threads = next_threads

        if len(threads):
            sublime.set_timeout(lambda: self.handle_threads(edit, threads, selections, offset, i), 100)
            return

        self.view.end_edit(edit)
        sublime.status_message('Successfully sorted')

    def handle_result(self, edit, thread, selections, offset):
        result = thread.result

        if thread.error:
            sublime.error_message(result)
            return
        elif result is None:
            sublime.error_message("There was an error sorting CSS.")
            return

        return thread


class CssSorter(BaseSorter):

    def handle_result(self, edit, thread, selections, offset):
        result = super(CssSorter, self).handle_result(edit, thread, selections, offset)

        sel = thread.sel
        result = to_unicode_or_bust(thread.result)

        if not thread.error:
            self.view.replace(edit, sel, result)
