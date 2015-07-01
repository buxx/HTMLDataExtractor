from sandbox.dalz.match import ArticleFileContentMatch, ArticleAndCommentsFileContentMatch
from tde.FileData import FileData
from tde.FilesData import FilesData
from tde.HTMLData import HTMLData

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
        return self._extract_text(text, selector_title)


class ArticleFilesData(FilesData, HTMLData):
    _match_class = ArticleFileContentMatch

    def _get_text_data_name(self, text):
        return self._extract_text(text, selector_title)


class ArticleAndCommentsFileData(ArticleFileData):
    _match_class = ArticleAndCommentsFileContentMatch


class ArticleCommentCountFileData(ArticleAndCommentsFileData):
    _name = 'Comments_count_by_article'
    _key_name = 'Article name'
    _value_name = 'Comments count'

    def _get_data_for_text(self, text):
        comments_count = self._extract_text(text, selector_comment)
        return self._re_extract_text(comments_count, pattern_comment_count)


class ArticlePublicationDateFileData(ArticleFileData):
    _name = 'Article_publication_date'
    _key_name = 'Article name'
    _value_name = 'Publication date'

    def _get_data_for_text(self, text):
        article_author = self._extract_text(text, selector_article_author)
        pattern = pattern_article_publication_date
        return self._re_extract_text(article_author, pattern, (2, 3), '%s %s')


class ArticleAuthorFileData(ArticleFileData):
    _name = 'Article_author'
    _key_name = 'Article name'
    _value_name = 'Author name'

    def _get_data_for_text(self, text):
        article_author = self._extract_text(text, selector_article_author)
        return self._re_extract_text(article_author, pattern_article_author)


class AuthorArticleCountFilesData(ArticleFilesData):
    _name = 'Author_articles_count'
    _key_name = 'Author name'
    _value_name = 'Articles count'

    def _get_text_data_name(self, text):
        article_author = self._extract_text(text, selector_article_author)
        return self._re_extract_text(article_author, pattern_article_author)

    def _get_data_for_text(self, text):
        return 1

    def _add_data(self, actual_data, new_data):
        return actual_data + new_data
