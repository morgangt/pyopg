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
        index_start = res.text.find(pattern) + len(pattern)

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
        tags_data = OgTags(
            title=self.get_value_tag(self.request, Pattern.pattern_title.value),
            description=self.get_value_tag(self.request, Pattern.pattern_description.value),
            image=self.get_value_tag(self.request, Pattern.pattern_image.value),
            site_name=self.get_value_tag(self.request, Pattern.pattern_site_name.value),
            )

        return tags_data

    def get_req(self) -> Request:
        """HTTP GET request."""
        result = None 

        with request.urlopen(self.url) as f:
            result = f.read().decode("utf-8")
            result = Request(text=result, status_code=f.getcode())

        return result


if __name__ == '__main__':
    tags = OpenGraph('https://www.imdb.com/title/tt0117500/')
    print(tags.tags)
    print(tags)
