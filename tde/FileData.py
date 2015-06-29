from tde.Data import Data


class FileData(Data):

    def _get_text_data_name(self, text):
        raise NotImplementedError()

    def _get_data_for_text(self, text):
        raise NotImplementedError()

    def _update_data_line(self, data_name, data):
        self._data[data_name] = data
