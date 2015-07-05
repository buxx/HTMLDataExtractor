from sandbox.dalz.data import ArticleCommentCountFileData, AuthorArticleCountFilesData, ArticlePublicationDateFileData, \
    ArticleAuthorFileData, ArticleWordCountFileData, CommentAuthorCommentCountFilesDatas
from sandbox.dalz.implode import ArticleImplode
from tde.CSVExporter import CSVExporter
from tde.Inspector import Inspector
from tde.Extractor import Extractor

# Répertoire ou les fichiers vont être exploré
source_directory = 'sandbox/dalz/Raw_Field_Blog/HTLML_complete/Blog_LaFraise/Blog_LaFraise/blog.lafraise.com/fr/'

# Les différentes données qui vont être extraites
data_classes = [ArticleCommentCountFileData,
                AuthorArticleCountFilesData,
                ArticlePublicationDateFileData,
                ArticleAuthorFileData,
                ArticleWordCountFileData,
                CommentAuthorCommentCountFilesDatas]

# Création de l'objet chargé de récupérer les fichiers correspondant aux données recherchés
inspector_lafraise = Inspector(source=source_directory,
                               data_classes=data_classes,
                               match_pattern='*.html')

# Création de l'extracteur de données
extractor = Extractor(inspectors=[inspector_lafraise])

# Extraction des données
data_collection = extractor.extract()

# Création de l'objet pour exporter en CSV. On précise la liste des données à compiler dans un fichier.
csv_convector = CSVExporter(data_collection, implode_classes=[ArticleImplode])

# Export dans le répertoire output des différentes données extraites
csv_convector.export('sandbox/dalz/output')

# TODO: Erreurs