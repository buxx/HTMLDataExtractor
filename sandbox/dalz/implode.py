from sandbox.dalz.data import ArticleCommentCountFileData, ArticlePublicationDateFileData, ArticleAuthorFileData
from tde.Implode import Implode


class ArticleImplode(Implode):
    _name = 'Articles'
    _data_classes = (ArticleCommentCountFileData,
                     ArticlePublicationDateFileData,
                     ArticleAuthorFileData)
