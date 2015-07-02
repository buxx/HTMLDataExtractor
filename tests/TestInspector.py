from tde.Inspector import Inspector
from tests.src.Base import Base
from tests.src.match import WikipediaTextFileContentMatch, WikipediaHTMLFileContentMatch


class TestInspector(Base):

    def test_inspect_wikipedia_text(self):
        inspector = Inspector('tests/src/source_files', self._wikipedia_text_data_classes, match_pattern='*.txt')
        self.assertEquals(self._wikipedia_text_data_classes, inspector.get_data_classes())

        self.assertEquals(self._wikipedia_text_files.sort(),
                          inspector.get_match_files(WikipediaTextFileContentMatch).sort())

        # With match pattern on all files, it will work to (but less speed)
        inspector = Inspector('tests/src/source_files', self._wikipedia_text_data_classes, match_pattern='*')
        self.assertEquals(self._wikipedia_text_files.sort(),
                          inspector.get_match_files(WikipediaTextFileContentMatch).sort())

    def test_inspect_wikipedia_html(self):
        inspector = Inspector('tests/src/source_files', self._wikipedia_html_data_classes, match_pattern='*.html')
        self.assertEquals(self._wikipedia_html_data_classes, inspector.get_data_classes())

        self.assertEquals(self._wikipedia_html_files.sort(),
                          inspector.get_match_files(WikipediaHTMLFileContentMatch).sort())

        # With match pattern on all files, it will work to (but less speed)
        inspector = Inspector('tests/src/source_files', self._wikipedia_html_data_classes, match_pattern='*')
        self.assertEquals(self._wikipedia_html_files.sort(),
                          inspector.get_match_files(WikipediaHTMLFileContentMatch).sort())
