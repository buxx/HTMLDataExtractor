from tde.Implode import Implode
from tests.src.data import WikipediaLetterCountTextFileData, WikipediaWordCountTextFileData, WikipediaSourceTextFileData, \
    BritannicaLetterCountTextFileData, BritannicaWordCountTextFileData, BritannicaSourceTextFileData, \
    WikipediaLetterCountHTMLFileData, WikipediaWordCountHTMLFileData, BritannicaLetterCountHTMLFileData, \
    BritannicaWordCountHTMLFileData, WikipediaSourceHTMLFileData, BritannicaSourceHTMLFileData


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


class WikipediaHTMLArticleImplode(Implode):
    _name = 'Wikipedia_Articles'
    _data_classes = (WikipediaLetterCountHTMLFileData,
                     WikipediaWordCountHTMLFileData,
                     WikipediaSourceHTMLFileData)


class BritannicaHTMLArticleImplode(Implode):
    _name = 'Britannica_Articles'
    _data_classes = (BritannicaLetterCountHTMLFileData,
                     BritannicaWordCountHTMLFileData,
                     BritannicaSourceHTMLFileData)

# TODO: Confondre des sources entre elles ?
# class ArticleImplode(Implode):
#     _name = 'Articles'
#     _data_classes = (WikipediaLetterCountTextFileData,
#                      WikipediaWordCountTextFileData,
#                      WikipediaSourceTextFileData,
#                      BritannicaLetterCountTextFileData,
#                      BritannicaWordCountTextFileData,
#                      BritannicaSourceTextFileData)
