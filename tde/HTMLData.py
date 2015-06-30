from pyquery import PyQuery
from tde.exceptions import CantExtractData


class HTMLData:

    @classmethod
    def _extract(cls, html, selector):
        d = PyQuery(html)
        nodes = d(selector)
        if not nodes.size():
            raise CantExtractData()
        return nodes

    @classmethod
    def _extract_text(cls, html, selector):
        return cls._extract(html, selector).text()