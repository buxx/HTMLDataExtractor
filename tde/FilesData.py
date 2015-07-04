from tde.Data import Data
from tde.exceptions import NoIdentifierMechanismSet


class FilesData(Data):

    def __init__(self):
        super().__init__()
        self._text_identifiers_proceeded = []

    def _get_text_data_name(self, text):
        raise NotImplementedError()

    def _get_data_for_text(self, text):
        raise NotImplementedError()

    def _update_data_line(self, data_name, data):
        if data_name not in self._data:
            self._data[data_name] = data
        else:
            self._data[data_name] = self._add_data(self._data[data_name], data)

    def _add_data(self, actual_data, new_data):
        raise NotImplementedError()

    def _get_text_identifier(self, text):
        raise NoIdentifierMechanismSet()

    def _can_take_into_account_text(self, text):
        text_identifier = self._get_text_identifier(text)
        if text_identifier not in self._text_identifiers_proceeded:
            self._text_identifiers_proceeded.append(text_identifier)
            return True
        return False
