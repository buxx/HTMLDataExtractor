from tde.DataBase import DataBase


class FileDatas(DataBase):

    def swallow(self, text):
        for data_set in self._get_data_sets(text):
            data_set_name = self._get_data_set_name(data_set)
            data_set_value = self._get_data_set_value(data_set)
            self._update_data_line(data_set_name, data_set_value)
    
    def _get_data_sets(self, text):
        raise NotImplementedError()

    def _get_data_set_name(self, data_set):
        raise NotImplementedError()

    def _get_data_set_value(self, data_set):
        raise NotImplementedError()
