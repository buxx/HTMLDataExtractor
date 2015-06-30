class Exporter:

    def __init__(self, data_collection, implode_classes=[]):
        self._data_collection = data_collection
        self._implode_classes = implode_classes

    def export(self, output_directory):
        raise NotImplementedError()
