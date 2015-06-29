from tde.FileContentMatch import FileContentMatch
from pyquery import PyQuery
from tde.exceptions import CantMakeMatch


class HTMLFileContentMatch(FileContentMatch):

    def __init__(self, file_path):
        super().__init__(file_path)

        try:
            self._parser = PyQuery(filename=file_path)
        except UnicodeDecodeError:
            raise CantMakeMatch()