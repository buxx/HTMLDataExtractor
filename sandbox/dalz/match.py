from tde.HTMLFileContentMatch import HTMLFileContentMatch


class ArticleFileContentMatch(HTMLFileContentMatch):
    def match(self):
        return bool(len(self._parser('div.blogitem')) == 1)

class ArticleAndCommentsFileContentMatch(HTMLFileContentMatch):
    def match(self):
        return len(self._parser('div.blogitem')) == 1 and len(self._parser('a.cmnt_count'))
