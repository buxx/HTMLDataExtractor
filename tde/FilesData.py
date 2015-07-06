from tde.FileData import FileData


class FilesData(FileData):

    def __init__(self):
        super().__init__()
        self._text_identifiers_proceeded = []

    def swallow(self, text):
        if self._can_take_into_account_text(text):
            text_data_name = self._get_text_data_name(text)
            text_data_value = self._get_data_for_text(text)
            self._update_data_line(text_data_name, text_data_value)

    def _update_data_line(self, data_name, data):
        if data_name not in self._data:
            self._data[data_name] = data
        else:
            self._data[data_name] = self._add_data(self._data[data_name], data, data_name)

    def _add_data(self, actual_data, new_data, data_name):
        raise NotImplementedError()

    def _get_text_identifier(self, text):
        raise NotImplementedError()

    def _can_take_into_account_text(self, text):
        text_identifier = self._get_text_identifier(text)
        if text_identifier not in self._text_identifiers_proceeded:
            self._text_identifiers_proceeded.append(text_identifier)
            return True
        return False
