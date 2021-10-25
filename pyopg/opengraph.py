from functools import partial
from model import Request, Pattern, OgTags

from typing import Text, Tuple, Union
from urllib import request


class OpenGraph:
    """Parsing opengraph tag site."""

    def __init__(self, url: str) -> None:
        self.url = url
        self.request = self.get_req()
        self.tags = self.get_og_tag()
        
    def __str__(self) -> str:
        return f'OpenGraph site: {self.tags.site_name}'

    @staticmethod
    def index_og_tag(res: Request, pattern: Pattern) -> Tuple:
        """Static method return index og:tag on pattern."""
        find_pattern = f'<meta property="og:{pattern}" content="'
        index_start = res.text.find(find_pattern) + len(find_pattern)

        index_finish = index_start + res.text[(index_start):].find('">')

        if '"/>' in res.text[index_start:index_finish]:
            index_finish = index_start + res.text[(index_start):].find('"/>')

        return (index_start, index_finish)

    def get_value_tag(self, document: Request, pattern: Pattern):
        """Geting value tag on pattern."""
        start, end = self.index_og_tag(document, pattern)
        return document.text[start:end]
    
    def get_og_tag(self) -> OgTags:
        """Return object OgTags with info."""
        tags_data = partial(OgTags)

        for item in Pattern:
            value = self.get_value_tag(self.request, item.value)
            if value: 
                tags_data = partial(tags_data, value)

        return tags_data()

    def get_req(self) -> Request:
        """HTTP GET request."""
        result = None 

        with request.urlopen(self.url) as f:
            result = f.read().decode("utf-8")
            result = Request(text=result, status_code=f.getcode())

        return result


if __name__ == '__main__':
    tags = OpenGraph('https://www.imdb.com/title/tt0117500/')
    tags = OpenGraph('https://russian.rt.com/russia/article/921081-koronavirus-maksimum-zabolevshie-ogranicheniya-qr-kody')
    print(tags.tags)
    print(tags)
