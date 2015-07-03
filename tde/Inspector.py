import fnmatch
import os
from tde.Error import Error
from tde.exceptions import CantMakeMatch


class Inspector:

    def __init__(self, source, data_classes, recursive=True, match_pattern='*'):
        self._source = source
        self._recursive = recursive
        self._match_pattern = match_pattern
        self._data_classes = data_classes
        self._match_files = {}
        self._errors = []
        self._inspect_files()

    def _inspect_files(self):
        match_classes = self._get_match_classes()

        for file_path in self._get_all_files():
            for match_class in match_classes:
                self._update_file_match(match_class, file_path)

    def _get_match_classes(self):
        match_classes = []

        for data_class in self._data_classes:
            match_classes.append(data_class.get_match_class())

        return list(set(match_classes))

    def _get_all_files(self):
        # tmp dev
        x = 0

        for root, dir_names, file_names in os.walk(self._source):

            x = x+1
            if x > 100:
                #raise StopIteration()
                pass

            for file_name in fnmatch.filter(file_names, self._match_pattern):
                yield os.path.join(root, file_name)

    def _update_file_match(self, match_class, file_path):
        try:
            matcher = match_class(file_path)
            if matcher.match():
                self._add_match(match_class, file_path)
        except CantMakeMatch as exc:
            self._errors.append(Error(file_path, Error.ACTION_MATCH, exc))

    def _add_match(self, match_class, file_path):
        if match_class not in self._match_files:
            self._match_files[match_class] = []
        self._match_files[match_class].append(file_path)

    def get_data_classes(self):
        return self._data_classes

    def get_errors(self):
        return self._errors

    def add_error(self, error):
        self._errors.append(error)

    def get_match_files(self, match_class):
        if match_class not in self._match_files:
            return []
        return self._match_files[match_class]