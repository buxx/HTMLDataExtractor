from pyquery import PyQuery
from tde.exceptions import CantExtractData


class HTMLData:

    @classmethod
    def _extract_html(cls, html, selector):
        d = PyQuery(html)
        nodes = d(selector)
        if not nodes.size():
            raise CantExtractData()
        return nodes

    @classmethod
    def _extract_html_text(cls, html, selector):
        return cls._extract_html(html, selector).text()
