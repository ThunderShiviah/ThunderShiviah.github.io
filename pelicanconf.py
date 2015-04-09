#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Thunder Shiviah'
SITENAME = u'Thunder Shiviah'
SITEURL = ''

EMAIL_ADDRESS = 'thunder@uoregon.edu'
GITHUB_ADDRESS = 'https://github.com/ThunderShiviah'
SO_ADDRESS = 'http://stackoverflow.com/users/3081184/thunder-shiviah'
THEME = 'crowsfoot'
PATH = 'content'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

ARTICLE_PATHS = ['blog']

MENUITEMS = [('blog', '/'), ('cv', '/misc/cv.pdf')]
TIMEZONE = 'Europe/Paris'
MARKUP = ('md', 'ipynb')
DEFAULT_LANG = u'en'
PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
