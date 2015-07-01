from pyquery import PyQuery
from tde.exceptions import CantExtractData
import re


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

    @classmethod
    def _re_extract_text(cls, text, expression, groups=(1,), format_extract="%s"):
        sre_match = re.search(expression, text)
        if not sre_match:
            raise CantExtractData("Expression \"%s\" not found in \"%s\"" % (expression, text))

        groups_text = []
        for group_position in groups:
            groups_text.append(sre_match.group(group_position))

        return format_extract % tuple(groups_text)