from tests.src.Base import Base
from tests.src.data import WikipediaLetterCountTextFileData, WikipediaWordCountTextFileData, \
    WikipediaCategoryCountTextFilesData, WikipediaLetterCountHTMLFileData, WikipediaWordCountHTMLFileData, \
    WikipediaCategoryCountHTMLFilesData


class TestInspector(Base):

    def _get_content_of_file(self, file_path):
        with open(file_path) as file_content:
            return file_content.read()

    def test_wikipedia_text_data(self):
        letter_count = WikipediaLetterCountTextFileData()
        letter_count.swallow(self._get_content_of_file('tests/src/source_files/evolution.txt'))
        self.assertEquals({'Évolution (biologie)': 55251}, letter_count.get_data())

        word_count = WikipediaWordCountTextFileData()
        word_count.swallow(self._get_content_of_file('tests/src/source_files/evolution.txt'))
        # TODO: L'ER pour compter le nb de mots est incorrecte ! Pas 9 du coups!
        self.assertEquals({'Évolution (biologie)': 1}, word_count.get_data())

        category_count = WikipediaCategoryCountTextFilesData()
        category_count.swallow(self._get_content_of_file('tests/src/source_files/evolution.txt'))
        self.assertEquals({'Science': 1}, category_count.get_data())
        category_count.swallow(self._get_content_of_file('tests/src/source_files/relativite.txt'))
        self.assertEquals({'Science': 2}, category_count.get_data())
        category_count.swallow(self._get_content_of_file('tests/src/source_files/poisonous.txt'))
        self.assertEquals({'Nature': 1, 'Science': 2}, category_count.get_data())

    def test_wikipedia_html_data(self):
        letter_count = WikipediaLetterCountHTMLFileData()
        letter_count.swallow(self._get_content_of_file('tests/src/source_files/evolution.html'))
        self.assertEquals({'Évolution (biologie)': 59883}, letter_count.get_data())

        word_count = WikipediaWordCountHTMLFileData()
        word_count.swallow(self._get_content_of_file('tests/src/source_files/evolution.html'))
        # TODO: L'ER pour compter le nb de mots est incorrecte ! Pas 9 du coups!
        self.assertEquals({'Évolution (biologie)': 1}, word_count.get_data())

        category_count = WikipediaCategoryCountHTMLFilesData()
        category_count.swallow(self._get_content_of_file('tests/src/source_files/evolution.html'))
        self.assertEquals({'Science': 1}, category_count.get_data())
        category_count.swallow(self._get_content_of_file('tests/src/source_files/relativite.html'))
        self.assertEquals({'Science': 2}, category_count.get_data())
        category_count.swallow(self._get_content_of_file('tests/src/source_files/poisonous.html'))
        self.assertEquals({'Nature': 1, 'Science': 2}, category_count.get_data())

    def test_not_found(self):
        # Tester quand on check un fichier qui a rien avoir: raise
        pass