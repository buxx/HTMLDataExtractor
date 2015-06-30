import re
from pyquery import PyQuery
from sandbox.dalz.match import ArticleFileContentMatch
from tde.FileData import FileData
from tde.FilesData import FilesData
from tde.HTMLData import HTMLData


class ArticleFileData(FileData, HTMLData):
    _match_class = ArticleFileContentMatch

    def _get_data_for_text(self, text):
        raise NotImplementedError()

    def _get_text_data_name(self, text):
        return self._extract_text(text, 'h1.entry-title')


class ArticleCommentCountFileData(ArticleFileData):
    _name = 'Comments_count_by_article'
    _key_name = 'Article name'
    _value_name = 'Comments count'

    def _get_data_for_text(self, text):
        comments_count = self._extract_text(text, 'a.cmnt_count')
        return re.search('^([0-9]+) Commentaires', comments_count).group(1)


class ArticlePublicationDateFileData(ArticleFileData):
    _name = 'Article_publication_date'
    _key_name = 'Article name'
    _value_name = 'Publication date'

    def _get_data_for_text(self, text):
        blog_author = self._extract_text(text, 'div.blogauthor div.left')
        pattern = '^De\ ([a-zA-Z0-9]+), le ([0-9]{2}\.[0-9]{2}\.[0-9]{4}) à ([0-9]{2}:[0-9]{2})'
        extract = re.search(pattern, blog_author)
        return "%s %s" % (extract.group(2), extract.group(3))


class ArticleAuthorFileData(ArticleFileData):
    _name = 'Article_author'
    _key_name = 'Article name'
    _value_name = 'Author name'

    def _get_data_for_text(self, text):
        blog_author = self._extract_text(text, 'div.blogauthor div.left')
        return re.search('^De\ ([a-zA-Z0-9]+),', blog_author).group(1)


class AuthorArticleCountFilesData(ArticleFileData):
    _name = 'Author_articles_count'
    _key_name = 'Author name'
    _value_name = 'Articles count'

    def _get_text_data_name(self, text):
        blog_author = self._extract_text(text, 'div.blogauthor div.left')
        return re.search('^De\ ([a-zA-Z0-9]+),', blog_author).group(1)

    def _get_data_for_text(self, text):
        return 1

    def _add_data(self, actual_data, new_data):
        return actual_data + new_data
