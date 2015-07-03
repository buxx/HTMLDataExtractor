import re
from tde.FileData import FileData
from tde.FilesData import FilesData
from tde.HTMLData import HTMLData
from tests.src.match import WikipediaTextFileContentMatch, WikipediaHTMLFileContentMatch, \
    BritannicaTextFileContentMatch, BritannicaHTMLFileContentMatch

wikipedia_text_data_name_pattern = '^(.*), depuis Wikipédia.'
britannica_text_data_name_pattern = '^(.*), from britannica.com.'

wikipedia_html_data_name_pattern = 'h1#firstHeading'
britannica_html_data_name_pattern = 'div#content > div > h1'


class TextFileData(FileData):
    _key_name = 'Article name'
    _data_name_pattern = None

    def _get_data_name_pattern(self):
        if self._data_name_pattern is None:
            raise NotImplementedError()
        return self._data_name_pattern

    def _get_text_data_name(self, text):
        return self._extract_text(text, self._get_data_name_pattern())


class LetterCountTextFileData(TextFileData):
    _name = 'Letter_count_by_article'
    _value_name = 'Letter count'

    def _get_data_for_text(self, text):
        return len(text) - text.count(' ')


class WordCountTextFileData(TextFileData):
    _name = 'Word_count_by_article'
    _value_name = 'Word count'

    def _get_data_for_text(self, text):
        return len(list(set(re.findall("(\S+)*", text))))


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


class HTMLFileData(TextFileData, HTMLData):

    def _get_text_data_name(self, text):
        return self._extract_html_text(text, self._get_data_name_pattern())


class LetterCountHTMLFileData(HTMLFileData, HTMLData):
    _name = 'Letter_count_by_article'
    _value_name = 'Letter count'

    def _get_data_for_text(self, text):
        content_text = self._extract_html_text(text, 'div#content')
        return len(content_text) - content_text.count(' ')


class WordCountHTMLFileData(HTMLFileData):
    _name = 'Word_count_by_article'
    _value_name = 'Word count'
    def _get_data_for_text(self, text):
        content_text = self._extract_html_text(text, 'div#content')
        return len(list(set(re.findall("(\S+)*", content_text))))


# TODO: Il va falloir une declinaison HTMLFilesData ?
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
    _data_name_pattern = wikipedia_text_data_name_pattern


class WikipediaWordCountTextFileData(WordCountTextFileData):
    _match_class = WikipediaTextFileContentMatch
    _data_name_pattern = wikipedia_text_data_name_pattern


class WikipediaCategoryCountTextFilesData(CategoryCountTextFilesData):
    _match_class = WikipediaTextFileContentMatch
    _data_name_pattern = wikipedia_text_data_name_pattern


class BritannicaLetterCountTextFileData(LetterCountTextFileData):
    _match_class = BritannicaTextFileContentMatch
    _data_name_pattern = britannica_text_data_name_pattern


class BritannicaWordCountTextFileData(WordCountTextFileData):
    _match_class = BritannicaTextFileContentMatch
    _data_name_pattern = britannica_text_data_name_pattern


class BritannicaCategoryCountTextFilesData(CategoryCountTextFilesData):
    _match_class = BritannicaTextFileContentMatch
    _data_name_pattern = britannica_text_data_name_pattern


class WikipediaLetterCountHTMLFileData(LetterCountHTMLFileData):
    _match_class = WikipediaHTMLFileContentMatch
    _data_name_pattern = wikipedia_html_data_name_pattern


class WikipediaWordCountHTMLFileData(WordCountHTMLFileData):
    _match_class = WikipediaHTMLFileContentMatch
    _data_name_pattern = wikipedia_html_data_name_pattern


class WikipediaCategoryCountHTMLFilesData(CategoryCountHTMLFilesData):
    _match_class = WikipediaHTMLFileContentMatch
    _data_name_pattern = wikipedia_html_data_name_pattern


class BritannicaLetterCountHTMLFileData(LetterCountHTMLFileData):
    _match_class = BritannicaHTMLFileContentMatch
    _data_name_pattern = britannica_html_data_name_pattern


class BritannicaWordCountHTMLFileData(WordCountHTMLFileData):
    _match_class = BritannicaHTMLFileContentMatch
    _data_name_pattern = britannica_html_data_name_pattern


class BritannicaCategoryCountHTMLFilesData(CategoryCountHTMLFilesData):
    _match_class = BritannicaHTMLFileContentMatch
    _data_name_pattern = britannica_html_data_name_pattern


class WikipediaSourceTextFileData(TextFileData):
    _match_class = WikipediaTextFileContentMatch
    _data_name_pattern = wikipedia_text_data_name_pattern
    _value_name = 'Source'

    def swallow(self, text):
        super().swallow(text)

    def _get_data_for_text(self, text):
        return 'Wikipédia'


class BritannicaSourceTextFileData(TextFileData):
    _match_class = BritannicaHTMLFileContentMatch
    _data_name_pattern = britannica_text_data_name_pattern
    _value_name = 'Source'

    def _get_data_for_text(self, text):
        return 'Britannica'
