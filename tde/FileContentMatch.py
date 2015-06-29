class FileContentMatch:

    def __init__(self, file_path):
        self._file_path = file_path

    def match(self):
        raise NotImplementedError()
