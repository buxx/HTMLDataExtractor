from tde.Data import Data


class FilesData(Data):

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