class Data:

    _match_class = None
    _subject = None
    _key_name = 'Key'
    _value_name = 'Value'

    @classmethod
    def get_subject(cls):
        if not cls._subject:
            raise NotImplementedError('_subject must be set')
        return cls._subject

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
