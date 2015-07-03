from tde.DataCollection import DataCollection
from tde.Error import Error
from tde.exceptions import CantExtractData


class Extractor:

    def __init__(self, inspectors):
        """

        :param inspectors: list of tde.Inspector.Inspector instances
        :type inspectors: list
        :return:
        """
        self._inspectors = inspectors
        self._data_classes = []
        for inspector in self._inspectors:
            self._data_classes.extend(inspector.get_data_classes())

    def extract(self):
        data_collection = DataCollection(self._get_data_instances())
        errors = []

        for inspector in self._inspectors:
            for data_instance in data_collection.get_data_instances():
                for file_path in inspector.get_match_files(data_instance.get_match_class()):
                    with open(file_path, 'r') as file_content:
                        try:
                            data_instance.swallow(file_content.read())
                        except CantExtractData as exc:
                            inspector.add_error(Error(file_path, Error.ACTION_DATA, exc))
            errors.extend(inspector.get_errors())

        data_collection.set_errors(errors)
        return data_collection

    def _get_files(self):
        files = []
        for inspector in self._inspectors:
            files.extend(inspector.get_files())
        return files

    def _get_data_instances(self):
        data_instances = []
        for data_class in self._data_classes:
            data_instances.append(data_class())
        return data_instances
