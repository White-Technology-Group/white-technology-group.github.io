import time

AUTHOR = 'Zack White'
SITENAME = 'White Technology Group'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en_US'

# Get the year to place in the copyright notice.
CURRENT_YEAR = time.strftime("%Y")

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (("Zack's Tech Blog", 'https://zackwhiteit.com/'),)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True