import fnmatch
import os
from tde.exceptions import CantMakeMatch


class Inspector:

    def __init__(self, source, match, recursive=True, match_pattern='*.html'):
        self._source = source
        self._recursive = recursive
        self._match_pattern = match_pattern
        self._match = match
        self._files_errors = {}

    def get_files(self):
        self._files_errors = {}
        matches = []

        for root, dir_names, file_names in os.walk(self._source):
            for file_name in fnmatch.filter(file_names, self._match_pattern):
                complete_file_name = os.path.join(root, file_name)
                if self._file_content_match(complete_file_name):
                    matches.append(os.path.join(root, complete_file_name))

            # dev
            if len(matches) > 10:
                return matches

        return matches

    def _file_content_match(self, file_name):
        try:
            match = self._match(file_name)
            return match.match()
        except CantMakeMatch as exc:
            self._files_errors[file_name] = exc
            return False

    def get_file_errors(self):
        return self._files_errors