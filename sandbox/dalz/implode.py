from sandbox.dalz.data import ArticleCommentCountFileData, ArticlePublicationDateFileData
from tde.Implode import Implode


class ArticleImplode(Implode):
    _name = 'Articles'
    _data_classes = (ArticleCommentCountFileData, ArticlePublicationDateFileData)
    _on_key = 'Article name'
