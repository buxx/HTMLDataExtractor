from tde.FileData import FileData
from tde.FilesData import FilesData
from tde.HTMLData import HTMLData
from tests.src.match import WikipediaTextFileContentMatch, WikipediaHTMLFileContentMatch, \
    BritannicaTextFileContentMatch, BritannicaHTMLFileContentMatch


class TextFileData(FileData):
    _key_name = 'Article name'

    def _get_text_data_name(self, text):
        return self._extract_text(text, '^(.*), depuis Wikipédia.')


class LetterCountTextFileData(TextFileData):
    _name = 'Letter_count_by_article'
    _value_name = 'Letter count'

    def _get_data_for_text(self, text):
        return len(text) - text.count(' ')


class WordCountTextFileData(TextFileData):
    _name = 'Word_count_by_article'
    _value_name = 'Word count'

    def _get_data_for_text(self, text):
        return len(self._extract_text(text, "(\S+)"))


class CategoryCountTextFilesData(FilesData):
    _name = 'Category_of_articles_count'
    _key_name = 'Category name'
    _value_name = 'Category count'

    def _get_text_data_name(self, text):
        return self._extract_text(text, 'Catégorie: (\S+).')

    def _get_data_for_text(self, text):
        return 1

    def _add_data(self, actual_data, new_data):
        return actual_data + new_data


class HTMLFileData(FileData, HTMLData):
    _match_class = WikipediaHTMLFileContentMatch
    _key_name = 'Article name'

    def _get_text_data_name(self, text):
        return self._extract_html_text(text, 'h1.firstHeading')


class LetterCountHTMLFileData(TextFileData, HTMLData):
    _name = 'Letter_count_by_article'
    _value_name = 'Letter count'

    def _get_data_for_text(self, text):
        content_text = self._extract_html_text(text, 'div#content').text()
        return len(content_text) - content_text.count(' ')


class WordCountHTMLFileData(TextFileData):
    _name = 'Word_count_by_article'
    _value_name = 'Word count'
# TODO: Pas generique entre wki et brita
    def _get_data_for_text(self, text):
        content_text = self._extract_html_text(text, 'div#content').text()
        return len(self._extract(content_text, "(\S+)"))


class CategoryCountHTMLFilesData(FilesData, HTMLData):
    _match_class = WikipediaHTMLFileContentMatch
    _name = 'Category_of_articles_count'
    _key_name = 'Category name'
    _value_name = 'Category count'

    def _get_text_data_name(self, text):
        meta_category = self._extract_html(text, 'meta[name="category"]')
        return meta_category.attr('content')

    def _get_data_for_text(self, text):
        return 1

    def _add_data(self, actual_data, new_data):
        return actual_data + new_data


class WikipediaLetterCountTextFileData(LetterCountTextFileData):
    _match_class = WikipediaTextFileContentMatch

class WikipediaWordCountTextFileData(WordCountTextFileData):
    _match_class = WikipediaTextFileContentMatch

class WikipediaCategoryCountTextFilesData(CategoryCountTextFilesData):
    _match_class = WikipediaTextFileContentMatch

    
class BritannicaLetterCountTextFileData(LetterCountTextFileData):
    _match_class = BritannicaTextFileContentMatch

class BritannicaWordCountTextFileData(WordCountTextFileData):
    _match_class = BritannicaTextFileContentMatch

class BritannicaCategoryCountTextFilesData(CategoryCountTextFilesData):
    _match_class = BritannicaTextFileContentMatch

    
class WikipediaLetterCountHTMLFileData(LetterCountHTMLFileData):
    _match_class = WikipediaHTMLFileContentMatch

class WikipediaWordCountHTMLFileData(WordCountHTMLFileData):
    _match_class = WikipediaHTMLFileContentMatch

class WikipediaCategoryCountHTMLFilesData(CategoryCountHTMLFilesData):
    _match_class = WikipediaHTMLFileContentMatch

    
class BritannicaLetterCountHTMLFileData(LetterCountHTMLFileData):
    _match_class = BritannicaHTMLFileContentMatch

class BritannicaWordCountHTMLFileData(WordCountHTMLFileData):
    _match_class = BritannicaHTMLFileContentMatch

class BritannicaCategoryCountHTMLFilesData(CategoryCountHTMLFilesData):
    _match_class = BritannicaHTMLFileContentMatch
