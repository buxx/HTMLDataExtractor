class TextDataExtractorException(Exception):
    pass


class CantMakeMatch(TextDataExtractorException):
    pass


class CantExtractData(TextDataExtractorException):
    pass


class NoIdentifierMechanismSet(TextDataExtractorException):
    pass