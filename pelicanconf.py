#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'the PrivateBin Project'
ABOUT_ME = 'PrivateBin is a minimalist, open source online pastebin where the server has zero knowledge of pasted data. Data is encrypted / decrypted in the browser using 256bit AES in Galois Counter mode.'
SITENAME = u'PrivateBin'
SITEURL = ''


PATH = 'content'
THEME = 'themes/privatebin-bootstrap'

TIMEZONE = 'Europe/Zurich'
LOCALE = ('en_US.utf8')
DATE_FORMATS = {
    'en': '%A, %d. %B %Y'
}
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Navigation
MENUITEMS = (('Wiki', 'https://github.com/PrivateBin/PrivateBin/wiki'),
             ('Issues', 'https://github.com/PrivateBin/PrivateBin/issues'),
             ('PHPDOC', '/phpdoc/'),
             ('Test Coverage', '/coverage/'),)

# Blogroll
LINKS = (('Project on GitHub', 'https://github.com/PrivateBin/PrivateBin'),
         ('Installation guide', 'https://github.com/PrivateBin/PrivateBin/wiki/Installation'),
         ('Upgrading from ZeroBin 0.19 Alpha', 'https://github.com/PrivateBin/PrivateBin/wiki/Upgrading-from-ZeroBin-0.19-Alpha'),
         ('Configuration guide', 'https://github.com/PrivateBin/PrivateBin/wiki/Configuration'),
         ('Template guide', 'https://github.com/PrivateBin/PrivateBin/wiki/Templates'),
         ('Developer guide', 'https://github.com/PrivateBin/PrivateBin/wiki/Development'),
         ('Report an issue', 'https://github.com/PrivateBin/PrivateBin/issues'),)

# Social widget
SOCIAL = ()

# Theme specific settings
DISPLAY_ARTICLE_INFO_ON_INDEX = True
GITHUB_RIBBON_URL = 'https://github.com/PrivateBin/PrivateBin'
NEW_BUTTON_URL = 'http://privatebin.net/'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
