import re
from sandbox.dalz.match import ArticleFileContentMatch, ArticleAndCommentsFileContentMatch
from tde.FileData import FileData
from tde.FilesData import FilesData
from tde.HTMLData import HTMLData
from datetime import datetime

# Selecteurs CSS
selector_title = 'h1.entry-title'
selector_comment = 'a.cmnt_count'
selector_article_author = 'div.blogauthor div.left'

# Pattern d'expressions régulières
pattern_comment_count = '^([0-9]+) Commentaire[s]*'
pattern_article_publication_date = '^De\ ([a-zA-Z0-9?]+), le ([0-9]{2}\.[0-9]{2}\.[0-9]{4}) à ([0-9]{2}:[0-9]{2})'
pattern_article_author = '^De\ ([a-zA-Z0-9?]+),'

class ArticleFileData(FileData, HTMLData):
    _match_class = ArticleFileContentMatch

    def _get_text_data_name(self, text):
        return self._extract_html_text(text, selector_title)


class ArticleFilesData(FilesData, HTMLData):
    _match_class = ArticleFileContentMatch

    def _get_text_data_name(self, text):
        return self._extract_html_text(text, selector_title)


class ArticleAndCommentsFileData(ArticleFileData):
    _match_class = ArticleAndCommentsFileContentMatch


class ArticleCommentCountFileData(ArticleAndCommentsFileData):
    _name = 'Comments_count_by_article'
    _key_name = 'Article name'
    _value_name = 'Comments count'

    def _get_data_for_text(self, text):
        comments_count = self._extract_html_text(text, selector_comment)
        return self._extract_text(comments_count, pattern_comment_count)


class ArticlePublicationDateFileData(ArticleFileData):
    _name = 'Article_publication_date'
    _key_name = 'Article name'
    _value_name = 'Publication date'

    def _get_data_for_text(self, text):
        article_author = self._extract_html_text(text, selector_article_author)
        article_date = self._extract_text(article_author, pattern_article_publication_date, (2, 3), '%s %s')
        re_match = re.search('^([0-9]{2})\.([0-9]{2})\.([0-9]{4}) ([0-9]{2}):([0-9]{2})', article_date)

        year = int(re_match.group(3))
        month = int(re_match.group(2))
        day = int(re_match.group(1))
        hour = int(re_match.group(4))
        minutes = int(re_match.group(5))

        date = datetime(year, month, day, hour, minutes)
        return date.isoformat(sep=' ')


class ArticleAuthorFileData(ArticleFileData):
    _name = 'Article_author'
    _key_name = 'Article name'
    _value_name = 'Author name'

    def _get_data_for_text(self, text):
        article_author = self._extract_html_text(text, selector_article_author)
        return self._extract_text(article_author, pattern_article_author)


class AuthorArticleCountFilesData(ArticleFilesData):
    _name = 'Author_articles_count'
    _key_name = 'Author name'
    _value_name = 'Articles count'

    def _get_text_data_name(self, text):
        article_author = self._extract_html_text(text, selector_article_author)
        return self._extract_text(article_author, pattern_article_author)

    def _get_data_for_text(self, text):
        if self._can_take_into_account_text(text):
            return 1
        return 0

    def _get_text_identifier(self, text):
        return self._extract_html_text(text, selector_title)

    def _add_data(self, actual_data, new_data):
        return actual_data + new_data
