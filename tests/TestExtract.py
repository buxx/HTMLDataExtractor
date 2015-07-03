from tests.src.Base import Base


class TestExtract(Base):

    def test_wikipedia_text_data(self):

        expected_value = {
            'Category_of_articles_count': {'Science': 2},
            'Letter_count_by_article': {'Relativité restreinte': 71720, 'Évolution (biologie)': 55251},
            'Word_count_by_article': {'Relativité restreinte': 3638, 'Évolution (biologie)': 3378}
        }

        data_collection = self._get_data_collection(self._wikipedia_text_data_classes, '*.txt')
        self.assertEquals(expected_value, data_collection.get_raw_data())

    def test_wikipedia_html_data(self):

        expected_value = {
            'Category_of_articles_count': {'Science': 2},
            'Letter_count_by_article': {'Relativité restreinte': 68678, 'Évolution (biologie)': 59883},
            'Word_count_by_article': {'Relativité restreinte': 3181, 'Évolution (biologie)': 3460}
        }

        data_collection = self._get_data_collection(self._wikipedia_html_data_classes, '*.html')
        self.assertEquals(expected_value, data_collection.get_raw_data())

    def test_britannica_text_data(self):

        expected_value = {
            'Letter_count_by_article': {'7 of the World’s Most Poisonous Mushrooms': 4650,
                                        ' Britannica Brush-ups: 12 Greek Gods and Goddesses': 6189},
            'Category_of_articles_count': {'Nature': 1, 'Religion': 1},
            'Word_count_by_article': {'7 of the World’s Most Poisonous Mushrooms': 413,
                                      ' Britannica Brush-ups: 12 Greek Gods and Goddesses': 573}
        }

        data_collection = self._get_data_collection(self._britannica_text_data_classes, '*.txt')
        self.assertEquals(expected_value, data_collection.get_raw_data())

    def test_britannica_html_data(self):

        expected_value = {
            'Category_of_articles_count': {'Nature': 1, 'Religion': 1},
            'Letter_count_by_article': {'7 of the World’s Most Poisonous Mushrooms': 5172,
                                        'Britannica Brush-ups: 12 Greek Gods and Goddesses': 6724},
            'Word_count_by_article': {'7 of the World’s Most Poisonous Mushrooms': 455,
                                      'Britannica Brush-ups: 12 Greek Gods and Goddesses': 615}
        }

        self.maxDiff = 2048
        data_collection = self._get_data_collection(self._britannica_html_data_classes, '*.html')
        self.assertDictEqual(expected_value, data_collection.get_raw_data())
