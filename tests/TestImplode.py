from tests.src.Base import Base
from tests.src.implode import WikipediaTextArticleImplode


class TestImplode(Base):

    def test_wikipedia_text_implode(self):
        data_collection = self._get_data_collection(WikipediaTextArticleImplode.get_data_classes(), '*.txt')
        implode = WikipediaTextArticleImplode(data_collection.get_data_instances())

        self.assertEquals(['Article name', 'Letter count', 'Word count', 'Source'], implode.get_header())
        self.assertEquals({
            'Relativité restreinte': [71720, 3638, 'Wikipédia'],
            'Évolution (biologie)': [55251, 3378, 'Wikipédia']
        }, implode.get_data())
