from tde.DataBase import DataBase


class FileData(DataBase):

    def swallow(self, text):
        text_data_name = self._get_text_data_name(text)
        text_data_value = self._get_data_for_text(text)
        self._update_data_line(text_data_name, text_data_value)

    def _get_text_data_name(self, text):
        raise NotImplementedError()

    def _get_data_for_text(self, text):
        raise NotImplementedError()

    def _update_data_line(self, data_name, data):
        self._data[data_name] = data
