from tde.Inspector import Inspector
from tde.Extractor import Extractor
from tde.HTMLFileContentMatch import HTMLFileContentMatch as BaseHTMLFileContentMatch

source_directory = 'sandbox/Raw_Field_Blog/HTLML_complete/Blog_LaFraise/Blog_LaFraise/blog.lafraise.com/fr/'


class FileContentMatch(BaseHTMLFileContentMatch):
    def match(self):
        return bool(len(self._parser('div.blogitem')) == 1)


class ArticleExtractor(Extractor):
    pass

inspector_lafraise = Inspector(source=source_directory, match=FileContentMatch)
extractor = ArticleExtractor(inspectors=[inspector_lafraise])

data = extractor.extract()

pass  # Exporter en CSV
