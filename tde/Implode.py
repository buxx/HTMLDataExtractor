class Implode:

    _name = None
    _data_classes = []

    @classmethod
    def get_name(cls):
        if not cls._name:
            raise NotImplementedError()
        return cls._name

    @classmethod
    def get_data_classes(cls):
        if not cls._data_classes:
            raise NotImplementedError()
        return sorted(cls._data_classes, key=lambda klass: klass.__name__)

    def __init__(self, data_instances):
        # TODO: Use no private attribute instead __class__.__name__ ?
        self._data_instances = sorted(data_instances, key=lambda instance: instance.__class__.__name__)

    def get_key(self):
        key = None
        for data_instance in self._data_instances:
            data_instance_key = data_instance.get_key_name()
            if data_instance_key == key or key is None:
                key = data_instance_key
            else:
                raise Exception(
                    "Datas are not working with same key: actual is \"%s\" and key is \"%s\"" % (key,
                                                                                                 data_instance_key))
        return key

    def get_data(self):
        data = self._get_empty_data()
        for data_instance in self._data_instances:
            data_instance_data = data_instance.get_data()
            for wanted_key in data:
                if wanted_key in data_instance_data:
                    data_instance_value = data_instance_data[wanted_key]
                    data[wanted_key].append(data_instance_value)
                else:
                    data[wanted_key].append(None)

        return data

    def _get_empty_data(self):
        empty_data = {}
        for data_instance in self._data_instances:
            data_instance_data = data_instance.get_data()
            for data_instance_key in data_instance_data:
                if data_instance_key not in empty_data:
                    empty_data[data_instance_key] = []

        return empty_data

    def get_header(self):
        header = [self.get_key()]

        for data_class in self.get_data_classes():
            header.append(data_class.get_value_name())

        return header
