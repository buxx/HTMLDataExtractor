from sandbox.dalz.data import ArticleCommentCountFileData, ArticlePublicationDateFileData, ArticleAuthorFileData, \
    ArticleWordCountFileData
from tde.Implode import Implode


class ArticleImplode(Implode):
    _name = 'Articles'
    _data_classes = (ArticleWordCountFileData,
                     ArticleCommentCountFileData,
                     ArticlePublicationDateFileData,
                     ArticleAuthorFileData)
