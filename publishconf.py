#!/usr/bin/env python
from __future__ import unicode_literals

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = "https://djphat.albertoconnor.ca"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/%s.atom.xml"

DELETE_OUTPUT_DIRECTORY = True
