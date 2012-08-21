import threading


class BaseSort(threading.Thread):

    def __init__(self, sel, original):
        self.sel = sel
        self.original = original
        self.result = None
        self.error = None
        threading.Thread.__init__(self)

    def exec_request(self):
        return

    def run(self):
        try:
            self.result = self.exec_request()
        except (OSError) as (e):
             self.error = True
             self.result = 'Sorter Error: attempt to sort non-existent file'