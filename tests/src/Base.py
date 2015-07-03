from collections import OrderedDict
import unittest
from tde.Extractor import Extractor
from tde.Inspector import Inspector
from tests.src.data import WikipediaLetterCountTextFileData, WikipediaWordCountTextFileData, \
    WikipediaCategoryCountTextFilesData, WikipediaLetterCountHTMLFileData, WikipediaWordCountHTMLFileData, \
    WikipediaCategoryCountHTMLFilesData, BritannicaLetterCountTextFileData, BritannicaWordCountTextFileData, \
    BritannicaCategoryCountTextFilesData, BritannicaLetterCountHTMLFileData, BritannicaCategoryCountHTMLFilesData, \
    BritannicaWordCountHTMLFileData


class Base(unittest.TestCase):
    _wikipedia_text_files = ['tests/src/source_files/evolution.txt',
                             'tests/src/source_files/relativite.txt']

    _britannica_text_files = ['tests/src/source_files/gods_and_goddesses.txt',
                              'tests/src/source_files/poisonous.txt']

    _wikipedia_html_files = ['tests/src/source_files/evolution.html',
                             'tests/src/source_files/relativite.html']

    _britannica_html_files = ['tests/src/source_files/gods_and_goddesses.html',
                              'tests/src/source_files/poisonous.html']

    _other_text_files = ['tests/src/source_files/aubergines_farcies.txt']

    _all_files = []
    _all_files.extend(_wikipedia_text_files)
    _all_files.extend(_britannica_text_files)
    _all_files.extend(_wikipedia_html_files)
    _all_files.extend(_britannica_html_files)

    _wikipedia_files = []
    _wikipedia_files.extend(_wikipedia_text_files)
    _wikipedia_files.extend(_wikipedia_html_files)

    _britannica_files = []
    _britannica_files.extend(_britannica_text_files)
    _britannica_files.extend(_britannica_html_files)

    _text_files = []
    _text_files.extend(_wikipedia_text_files)
    _text_files.extend(_britannica_text_files)

    _html_files = []
    _html_files.extend(_wikipedia_html_files)
    _html_files.extend(_britannica_html_files)

    _wikipedia_text_data_classes = [WikipediaLetterCountTextFileData,
                                    WikipediaWordCountTextFileData,
                                    WikipediaCategoryCountTextFilesData]

    _wikipedia_html_data_classes = [WikipediaLetterCountHTMLFileData,
                                    WikipediaWordCountHTMLFileData,
                                    WikipediaCategoryCountHTMLFilesData]

    _britannica_text_data_classes = [BritannicaLetterCountTextFileData,
                                     BritannicaWordCountTextFileData,
                                     BritannicaCategoryCountTextFilesData]

    _britannica_html_data_classes = [BritannicaLetterCountHTMLFileData,
                                     BritannicaWordCountHTMLFileData,
                                     BritannicaCategoryCountHTMLFilesData]


    def _get_inspector(self, data_classes, match_pattern):
        return Inspector(source='tests/src/source_files',
                         data_classes=data_classes,
                         match_pattern=match_pattern)

    def _get_extractor(self, inspectors):
        return Extractor(inspectors=inspectors)

    def _get_data_collection(self, data_classes, match_pattern):
        inspector = self._get_inspector(data_classes, match_pattern)
        extractor = self._get_extractor([inspector])
        return extractor.extract()
