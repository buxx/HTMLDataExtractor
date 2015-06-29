

class Extractor:

    def __init__(self, inspectors):
        self._inspectors = inspectors

    def extract(self):
        files = self._get_files()
        return {}

    def _get_files(self):
        files = []
        for inspector in self._inspectors:
            files.extend(inspector.get_files())
        return files
