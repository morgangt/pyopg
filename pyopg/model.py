from dataclasses import dataclass
from enum import Enum


class Pattern(Enum):
    """List pattern."""
    pattern_title = '<meta property=\"og:title\" content=\"'
    pattern_image = '<meta property=\"og:image\" content=\"'
    pattern_description = '<meta property=\"og:description\" content=\"'
    pattern_site_name = '<meta property=\"og:site_name\" content=\"'

    def get_pattern(self):
        return 


@dataclass
class OgTags:
    """Open graph tag."""
    title: str
    description: str
    image: str
    site_name: str


@dataclass
class Request:
    """Requests object."""
    text: str
    status_code: int
