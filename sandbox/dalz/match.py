from tde.HTMLFileContentMatch import HTMLFileContentMatch


class ArticleFileContentMatch(HTMLFileContentMatch):
    def match(self):
        return bool(len(self._parser('div.blogitem')) == 1)