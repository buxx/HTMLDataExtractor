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
        return cls._data_classes

    def __init__(self, data_instances):
        self._data_instances = data_instances

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
        data = {}
        for data_instance in self._data_instances:
            data_instance_data = data_instance.get_data()
            for data_instance_key in data_instance_data:
                data_instance_value = data_instance_data[data_instance_key]

                if data_instance_key not in data:
                    data[data_instance_key] = []

                data[data_instance_key].append(data_instance_value)

        return data
