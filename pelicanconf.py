#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Fonzie'
SITENAME = 'Unended Quest'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Hong_Kong'

DEFAULT_LANG = 'zh'
LOCALE = 'zh_CN.UTF-8'

DATE_FORMATS = {
        'en': ((u'en_US', 'utf8'), u'%Y-%m-%d',),
        'zh': ((u'zh_CN', 'utf8'), u'%Y-%m-%d',),
}

#USE_FOLDER_AS_CATEGORY = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 8

STATIC_PATHS = ['images',
                'file'] 

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

PLUGIN_PATHS = ['plugins']
THEME = 'themes/pelican-dark-theme'

#PLUGINS = ['extract_toc']
#SITEMAP = {'format': 'xml'}

LOAD_CONTENT_CACHE = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
CHECK_MODIFIED_METHORD = 'md5'

#PYGMENTS_STYLE = 'desert'
GITHUB_USER = 'HtwoO'
GITHUB_SHOW_USER_LINK = True
CC_LICENSE = 'CC-BY-NC-SA'

#AVATAR = 'images/avatar.jpg'
#ABOUT_PAGE = 'about.html'

