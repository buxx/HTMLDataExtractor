from tde.Implode import Implode
from tests.src.data import WikipediaLetterCountTextFileData, WikipediaWordCountTextFileData, WikipediaSourceTextFileData, \
    BritannicaLetterCountTextFileData, BritannicaWordCountTextFileData, BritannicaSourceTextFileData


class WikipediaTextArticleImplode(Implode):
    _name = 'Wikipedia_Articles'
    _data_classes = (WikipediaLetterCountTextFileData,
                     WikipediaWordCountTextFileData,
                     WikipediaSourceTextFileData)


class BritannicaTextArticleImplode(Implode):
    _name = 'Britannica_Articles'
    _data_classes = (BritannicaLetterCountTextFileData,
                     BritannicaWordCountTextFileData,
                     BritannicaSourceTextFileData)

# TODO: Confondre des sources entre elles ?
# class ArticleImplode(Implode):
#     _name = 'Articles'
#     _data_classes = (WikipediaLetterCountTextFileData,
#                      WikipediaWordCountTextFileData,
#                      WikipediaSourceTextFileData,
#                      BritannicaLetterCountTextFileData,
#                      BritannicaWordCountTextFileData,
#                      BritannicaSourceTextFileData)
