from tde.Extractor import Extractor
from tde.Inspector import Inspector
from tde.exceptions import CantExtractData, CantMakeMatch
from tests.src.Base import Base
from tests.src.data import WikipediaSourceHTMLFileData
from tests.src.match import WikipediaHTMLFileContentMatch


class TestErrors(Base):

    def test_cant_match(self):
        self.assertRaises(CantMakeMatch,
                          WikipediaHTMLFileContentMatch,
                          'tests/src/source_files_errors/error_unicode.html')

    def test_cant_extract(self):
        wikipedia_html_data = WikipediaSourceHTMLFileData()
        with open('tests/src/source_files/evolution.txt') as file_content:
            self.assertRaises(CantExtractData, wikipedia_html_data.swallow, file_content.read())

    def test_errors_report(self):
        inspector = Inspector(source='tests/src/source_files_errors',
                              data_classes=self._wikipedia_html_data_classes,
                              match_pattern='*.html')
        extractor = Extractor(inspectors=[inspector])
        data_collection = extractor.extract()

        errors = data_collection.get_errors()
        self.assertEquals(1, len(errors))
        self.assertEquals(('tests/src/source_files_errors/error_unicode.html',
                           'match',
                           "'utf-8' codec can't decode byte 0xe0 in position 6071: invalid "
                           'continuation byte'), errors[0].get_as_tuple())
