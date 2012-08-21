import subprocess
from os import path, name

from basesort import BaseSort

__file__ = path.normpath(path.abspath(__file__))
__path__ = path.dirname(__file__)
libs_path = path.join(__path__, 'libs')
csscomb_path = path.join(libs_path, 'call_string.php')


class LocalSort(BaseSort):
    startupinfo = None
    if name == 'nt':
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE

    def check_php_on_path(self):
        try:
            subprocess.call('php -v', shell=False, startupinfo=self.startupinfo)
        except (OSError):
            self.error = True
            self.result = 'Unable find php.exe. Make sure it is available in your PATH.'

    def exec_request(self):
        if not self.error:
            myprocess = subprocess.Popen(['php', csscomb_path, self.original], shell=False, stdout=subprocess.PIPE, startupinfo=self.startupinfo)
            (sout, serr) = myprocess.communicate()
            myprocess.wait()

        if len(sout) > 0:
            return sout
        else:
            return None

    def run(self):
        self.check_php_on_path()
        try:
            self.result = self.exec_request()
        except (OSError):
            self.error = True
            self.result = 'Sorter Error: attempt to sort non-existent file'
