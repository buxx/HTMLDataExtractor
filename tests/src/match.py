from tde.HTMLFileContentMatch import HTMLFileContentMatch
from tde.FileContentMatch import FileContentMatch


class WikipediaTextFileContentMatch(FileContentMatch):
    def match(self):
        return self._file_contain(', depuis Wikipédia.')


class WikipediaHTMLFileContentMatch(HTMLFileContentMatch):
    def match(self):
        return len(self._parser('meta[name="generator"][content^="MediaWiki"]')) == 1


class BritannicaTextFileContentMatch(FileContentMatch):
    def match(self):
        return self._file_contain(', from britannica.com.')


class BritannicaHTMLFileContentMatch(HTMLFileContentMatch):
    def match(self):
        return len(self._parser('meta[content="Encyclopedia Britannica"]')) == 1
