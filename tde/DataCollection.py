class DataCollection:

    def __init__(self, data_instances=[]):
        self._data_instances = data_instances

    def add_data_instances(self, data_instances):
        self._data_instances.extend(data_instances)

    def get_data_instances(self):
        return self._data_instances

    def get_raw_data(self):
        raw_data = {}
        for data_instance in self.get_data_instances():
            raw_data[data_instance.get_name()] = data_instance.get_data()
        return raw_data
