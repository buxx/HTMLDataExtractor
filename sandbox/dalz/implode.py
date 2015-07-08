from sandbox.dalz.data import ArticleCommentCountFileData, ArticlePublicationDateFileData, ArticleAuthorFileData, \
    ArticleWordCountFileData, CommentAuthorCommentCountFilesDatas, AuthorArticleCountFilesData, \
    AuthorArticlesCommentsCountAverageFilesData, AuthorArticlesWordsCountAverageFilesData, \
    ArticlePublicationHourFileData, ArticlePatriceCommentCountFileData
from tde.Implode import Implode


class ArticleImplode(Implode):
    _name = 'Articles'
    _data_classes = [ArticleWordCountFileData,
                     ArticleCommentCountFileData,
                     ArticlePublicationDateFileData,
                     ArticlePublicationHourFileData,
                     ArticleAuthorFileData,
                     ArticlePatriceCommentCountFileData]


class AuthorImplode(Implode):
    _name = 'Authors'
    _data_classes = [AuthorArticleCountFilesData,
                     AuthorArticlesCommentsCountAverageFilesData,
                     AuthorArticlesWordsCountAverageFilesData]
