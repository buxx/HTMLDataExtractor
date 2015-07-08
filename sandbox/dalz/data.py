import re
from sandbox.dalz.match import ArticleFileContentMatch, ArticleAndCommentsFileContentMatch
from tde.FileData import FileData
from tde.FilesData import FilesData
from tde.FilesDatas import FilesDatas
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


class ArticleFilesDatas(FilesDatas, HTMLData):
    _match_class = ArticleFileContentMatch


class ArticleAndCommentsFileData(ArticleFileData):
    _match_class = ArticleAndCommentsFileContentMatch


class ArticleCommentCountFileData(ArticleAndCommentsFileData):
    _name = 'Comments_count_by_article'
    _key_name = 'Article name'
    _value_name = 'Comments count'

    def _get_data_for_text(self, text):
        comments_count = self._extract_html_text(text, selector_comment)
        return self._extract_text(comments_count, pattern_comment_count)


class ArticleWordCountFileData(ArticleAndCommentsFileData):
    _name = 'Words_count_by_article'
    _key_name = 'Article name'
    _value_name = 'Word count'

    def _get_data_for_text(self, text):
        content_text = self._extract_html_text(text, 'div.entry-content')
        return len(list(set(re.findall("(\S+)*", content_text))))


class ArticlePublicationDateFileData(ArticleFileData):
    _name = 'Article_publication_date'
    _key_name = 'Article name'
    _value_name = 'Publication date'

    def _get_data_for_text(self, text):
        article_author = self._extract_html_text(text, selector_article_author)
        article_date = self._extract_text(article_author, pattern_article_publication_date, (2,))
        re_match = re.search('^([0-9]{2})\.([0-9]{2})\.([0-9]{4})', article_date)

        year = int(re_match.group(3))
        month = int(re_match.group(2))
        day = int(re_match.group(1))

        return '%s-%s-%s' % (year, month, day)


class ArticlePublicationHourFileData(ArticleFileData):
    _name = 'Article_publication_hour'
    _key_name = 'Article name'
    _value_name = 'Publication hour'

    def _get_data_for_text(self, text):
        article_author = self._extract_html_text(text, selector_article_author)
        article_hour = self._extract_text(article_author, pattern_article_publication_date, (3,))
        return article_hour


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
        return 1

    def _get_text_identifier(self, text):
        return self._extract_html_text(text, selector_title)

    def _add_data(self, actual_data, new_data, data_name):
        return actual_data + new_data


class CommentAuthorCommentCountFilesDatas(FilesDatas, HTMLData):
    _match_class = ArticleAndCommentsFileContentMatch
    _name = 'Comment_Author_comments_count'
    _key_name = 'Comment author name'
    _value_name = 'Comments count'

    def _get_text_identifier(self, text):
        return self._extract_html_text(text, selector_title)

    def _get_data_sets(self, text):
        return self._extract_html(text, 'div#comments-div ol.commentlist > li')

    def _get_data_set_name(self, data_set):
        return self._extract_html_text(data_set, 'cite:first')

    def _get_data_set_value(self, set_text):
        return 1

    def _add_data(self, actual_data, new_data, data_name):
        return actual_data + new_data


class AuthorArticlesCommentsCountAverageFilesData(FilesData, HTMLData):
    _match_class = ArticleAndCommentsFileContentMatch
    _name = 'Author_articles_comments_count_average'
    _key_name = 'Author name'
    _value_name = 'Comments count average'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._data_count = {}

    def _get_text_identifier(self, text):
        return self._extract_html_text(text, selector_title)

    def _add_data(self, actual_data, new_data, data_name):
        if data_name not in self._data_count:
            self._data_count[data_name] = 0
        self._data_count[data_name] += 1
        return int(actual_data) + int(new_data)

    def _get_data_for_text(self, text):
        comments_count = self._extract_html_text(text, selector_comment)
        return self._extract_text(comments_count, pattern_comment_count)

    def _get_text_data_name(self, text):
        article_author = self._extract_html_text(text, selector_article_author)
        return self._extract_text(article_author, pattern_article_author)

    def finalize(self):
        for data_name in self._data_count:
            data_count = self._data_count[data_name]
            self._data[data_name] = int(self._data[data_name]) / data_count


class AuthorArticlesWordsCountAverageFilesData(FilesData, HTMLData):
    _match_class = ArticleAndCommentsFileContentMatch
    _name = 'Author_articles_words_count_average'
    _key_name = 'Author name'
    _value_name = 'Words count average'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._data_count = {}

    def _get_text_identifier(self, text):
        return self._extract_html_text(text, selector_title)

    def _add_data(self, actual_data, new_data, data_name):
        if data_name not in self._data_count:
            self._data_count[data_name] = 0
        self._data_count[data_name] += 1
        return int(actual_data) + int(new_data)

    def _get_data_for_text(self, text):
        content_text = self._extract_html_text(text, 'div.entry-content')
        return len(list(set(re.findall("(\S+)*", content_text))))

    def _get_text_data_name(self, text):
        article_author = self._extract_html_text(text, selector_article_author)
        return self._extract_text(article_author, pattern_article_author)

    def finalize(self):
        for data_name in self._data_count:
            data_count = self._data_count[data_name]
            self._data[data_name] = int(self._data[data_name]) / data_count
