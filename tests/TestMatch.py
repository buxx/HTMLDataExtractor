import unittest
from tests.src.match import WikipediaTextFileContentMatch, WikipediaHTMLFileContentMatch, BritannicaHTMLFileContentMatch, \
    BritannicaTextFileContentMatch


class TestMatch(unittest.TestCase):

    _wikipedia_text_files = ['tests/src/source_files/evolution.txt',
                             'tests/src/source_files/relativite.txt']

    _britannica_text_files = ['tests/src/source_files/gods_and_goddesses.txt',
                              'tests/src/source_files/poisonous.txt']

    _wikipedia_html_files = ['tests/src/source_files/evolution.html',
                             'tests/src/source_files/relativite.html']

    _britannica_html_files = ['tests/src/source_files/gods_and_goddesses.html',
                              'tests/src/source_files/poisonous.html']

    def test_wikipedia_text(self):

        for wikipedia_text_file in self._wikipedia_text_files:
            text_matcher = WikipediaTextFileContentMatch(wikipedia_text_file)
            self.assertTrue(text_matcher.match())

        for britannica_text_file in self._britannica_text_files:
            text_matcher = WikipediaTextFileContentMatch(britannica_text_file)
            self.assertFalse(text_matcher.match())

    def test_wikipedia_html(self):

        for wikipedia_html_file in self._wikipedia_html_files:
            html_matcher = WikipediaHTMLFileContentMatch(wikipedia_html_file)
            self.assertTrue(html_matcher.match())

        for britannica_html_file in self._britannica_html_files:
            html_matcher = WikipediaHTMLFileContentMatch(britannica_html_file)
            self.assertFalse(html_matcher.match())

    def test_britannica_text(self):

        for wikipedia_text_file in self._wikipedia_text_files:
            text_matcher = BritannicaTextFileContentMatch(wikipedia_text_file)
            self.assertFalse(text_matcher.match())

        for britannica_text_file in self._britannica_text_files:
            text_matcher = BritannicaTextFileContentMatch(britannica_text_file)
            self.assertTrue(text_matcher.match())

    def test_britannica_html(self):

        for wikipedia_html_file in self._wikipedia_html_files:
            html_matcher = BritannicaHTMLFileContentMatch(wikipedia_html_file)
            self.assertFalse(html_matcher.match())

        for britannica_html_file in self._britannica_html_files:
            html_matcher = BritannicaHTMLFileContentMatch(britannica_html_file)
            self.assertTrue(html_matcher.match())
