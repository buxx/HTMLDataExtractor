from tests.src.Base import Base
from tests.src.implode import WikipediaTextArticleImplode, BritannicaTextArticleImplode, WikipediaHTMLArticleImplode, \
    BritannicaHTMLArticleImplode


class TestImplode(Base):

    def test_wikipedia_text_implode(self):
        data_collection = self._get_data_collection(WikipediaTextArticleImplode.get_data_classes(), '*.txt')
        implode = WikipediaTextArticleImplode(data_collection.get_data_instances())

        self.assertEquals(['Article name', 'Letter count', 'Source', 'Word count'], implode.get_header())
        self.assertDictEqual({
            'Relativité restreinte': [71720, 'Wikipédia', 3638],
            'Évolution (biologie)': [55251, 'Wikipédia', 3378]
        }, implode.get_data())

    def test_britannica_text_implode(self):
        data_collection = self._get_data_collection(BritannicaTextArticleImplode.get_data_classes(), '*.txt')
        implode = BritannicaTextArticleImplode(data_collection.get_data_instances())

        self.assertEquals(['Article name', 'Letter count', 'Source', 'Word count'], implode.get_header())
        self.assertDictEqual({
            ' Britannica Brush-ups: 12 Greek Gods and Goddesses': [6189, 'Britannica', 573],
            '7 of the World’s Most Poisonous Mushrooms': [4650, 'Britannica', 413]
        }, implode.get_data())

    def test_wikipedia_html_implode(self):
        data_collection = self._get_data_collection(WikipediaHTMLArticleImplode.get_data_classes(), '*.html')
        implode = WikipediaHTMLArticleImplode(data_collection.get_data_instances())

        self.assertEquals(['Article name', 'Letter count', 'Source', 'Word count'], implode.get_header())
        self.assertDictEqual({
            'Relativité restreinte': [68678, 'Wikipédia', 3181],
            'Évolution (biologie)': [59883, 'Wikipédia', 3460]
        }, implode.get_data())

    def test_britannica_html_implode(self):
        data_collection = self._get_data_collection(BritannicaHTMLArticleImplode.get_data_classes(), '*.html')
        implode = BritannicaHTMLArticleImplode(data_collection.get_data_instances())

        self.assertEquals(['Article name', 'Letter count', 'Source', 'Word count'], implode.get_header())
        self.assertDictEqual({
            'Britannica Brush-ups: 12 Greek Gods and Goddesses': [6724, 'Britannica', 615],
            '7 of the World’s Most Poisonous Mushrooms': [5172, 'Britannica', 455]
        }, implode.get_data())

    def test_wikipedia_and_britannica_text_implode(self):
        pass