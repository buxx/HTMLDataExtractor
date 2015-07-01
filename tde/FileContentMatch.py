class FileContentMatch:

    def __init__(self, file_path):
        self._file_path = file_path

    def _get_text(self):
        with open(self._file_path) as file_content:
            return file_content.read()

    def _file_contain(self, search_text):
        return self._get_text().find(search_text) != -1

    def match(self):
        raise NotImplementedError()
