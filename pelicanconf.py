#!/usr/bin/env python
from __future__ import unicode_literals

AUTHOR = "DJ Phat Albert"
SITENAME = "DJ Phat Albert"
SITEURL = ""

PATH = "content"
STATIC_PATHS = ["images", "extra/robots.txt", "extra/CNAME"]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/CNAME": {"path": "CNAME"},
}

TIMEZONE = "America/Toronto"
DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

THEME = "theme"
THEME_STATIC_DIR = "theme"
