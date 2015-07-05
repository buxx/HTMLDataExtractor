from tde.exceptions import NoIdentifierMechanismSet


class FilesDatasBase():

    def __init__(self):
        super().__init__()
        self._text_identifiers_proceeded = []

    def swallow(self, text):
        for data_set in self._get_data_sets(text):
            if self._can_take_into_account_text(text):
                data_set_name = self._get_data_set_name(data_set)
                data_set_value = self._get_data_set_value(data_set)
                self._update_data_line(data_set_name, data_set_value)

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
