class DataCollection:

    def __init__(self, data_instances=[]):
        self._data_instances = data_instances
        self._errors = []

    def add_data_instances(self, data_instances):
        self._data_instances.extend(data_instances)

    def get_data_instances(self):
        return self._data_instances

    def get_raw_data(self):
        raw_data = {}
        for data_instance in self.get_data_instances():
            data_instance_name = data_instance.get_name()
            if data_instance_name not in raw_data:
                raw_data[data_instance_name] = data_instance.get_data()
            else:
                raw_data[data_instance_name].update(data_instance.get_data())
        return raw_data

    def set_errors(self, errors):
        self._errors = errors

    def get_errors(self):
        return self._errors
