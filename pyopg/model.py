from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Pattern(Enum):
    """List pattern."""
    title = 'title'
    type = 'type'
    image = 'image'
    url = 'url'
    # optional
    audio = 'audio'
    determiner = 'determiner'
    locale = 'locale'
    locale_alternate = 'locale:alternate'
    video = 'video'
    site_name = 'site_name'
    description = 'description'


@dataclass
class OgTags:
    """Open graph tag."""
    # Basic Metadata
    title: str
    type: str
    image: str
    url: str
    # Optional Metadata
    audio: Optional[str] = None
    determiner: Optional[str] = None
    locale: Optional[str] = None
    locale_alternate: Optional[str] = None
    video: Optional[str] = None
    site_name: Optional[str] = None
    description: Optional[str] = None 


@dataclass
class Request:
    """Requests object."""
    text: str
    status_code: int
