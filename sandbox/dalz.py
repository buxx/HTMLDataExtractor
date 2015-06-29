from tde.FileData import FileData
from tde.FilesData import FilesData
from tde.Inspector import Inspector
from tde.Extractor import Extractor
from tde.HTMLFileContentMatch import HTMLFileContentMatch as BaseHTMLFileContentMatch
from pyquery import PyQuery
import re

source_directory = 'sandbox/Raw_Field_Blog/HTLML_complete/Blog_LaFraise/Blog_LaFraise/blog.lafraise.com/fr/'


class ArticleFileContentMatch(BaseHTMLFileContentMatch):
    def match(self):
        return bool(len(self._parser('div.blogitem')) == 1)


class ArticleExtractor(Extractor):
    pass


class ArticleCommentCountFileData(FileData):

    _match_class = ArticleFileContentMatch
    _subject = 'Comments_count_by_article'

    def _get_text_data_name(self, text):
        d = PyQuery(text)
        title_node = d('h1.entry-title')
        # TODO: Si pas de title, raise ...
        return title_node.text()

    def _get_data_for_text(self, text):
        d = PyQuery(text)
        comments_count_node = d('a.cmnt_count')
        # TODO: Si pas ... raise
        return comments_count_node.text()


class AuthorArticleCountFilesData(FilesData):

    _match_class = ArticleFileContentMatch
    _subject = 'Author_articles_count'

    def _get_text_data_name(self, text):
        d = PyQuery(text)
        blog_author_node = d('div.blogauthor div.left')
        # TODO: Si pas ... raise
        complete_author_line = blog_author_node.text()
        #  '^De\ (.)+,[.]+'
        return re.search('^De\ ([a-zA-Z0-9]+),', blog_author_node.text()).group(1)

    def _get_data_for_text(self, text):
        return 1

    def _add_data(self, actual_data, new_data):
        return actual_data + new_data

inspector_lafraise = Inspector(source=source_directory,
                               data_classes=[ArticleCommentCountFileData,
                                             AuthorArticleCountFilesData],
                               match_pattern='*.html')
extractor = ArticleExtractor(inspectors=[inspector_lafraise])

data = extractor.extract()

pass  # Exporter en CSV
