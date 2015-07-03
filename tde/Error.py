class Error:

    ACTION_MATCH = 'match'
    ACTION_DATA = 'data'

    def __init__(self, file_path, action, exception):
        self._file_path = file_path
        self._action = action
        self._exception = exception

    def get_as_tuple(self):
        return self._file_path, self._action, str(self._exception)
