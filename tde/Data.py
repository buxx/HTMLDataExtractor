import re
from tde.exceptions import CantExtractData


class Data:

    _match_class = None
    _name = None
    _key_name = 'Key'
    _value_name = 'Value'

    @classmethod
    def get_name(cls):
        if not cls._name:
            raise NotImplementedError('_name must be set')
        return cls._name

    @classmethod
    def get_match_class(cls):
        if not cls._match_class:
            raise NotImplementedError('_match_class must be set')
        return cls._match_class

    @classmethod
    def get_key_name(cls):
        return cls._key_name

    @classmethod
    def get_value_name(cls):
        return cls._value_name

    @classmethod
    def _extract_text(cls, text, expression, groups=(1,), format_extract="%s"):
        sre_match = cls._extract(expression, text)
        if not sre_match:
            raise CantExtractData("Expression \"%s\" not found in \"%s\"" % (expression, text))

        groups_text = []
        for group_position in groups:
            groups_text.append(sre_match.group(group_position))

        return format_extract % tuple(groups_text)

    @classmethod
    def _extract(cls, text, expression):
        return re.search(expression, text)

    def __init__(self):
        self._data = {}

    def swallow(self, text):
        text_data_name = self._get_text_data_name(text)
        self._update_data_line(text_data_name, self._get_data_for_text(text))
    
    def _get_text_data_name(self, text):
        raise NotImplementedError()
    
    def _get_data_for_text(self, text):
        raise NotImplementedError()

    def _update_data_line(self, data_name, data):
        raise NotImplementedError()

    def get_data(self):
        return self._data
