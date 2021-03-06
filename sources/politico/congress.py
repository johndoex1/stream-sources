from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'Politico',
        'category': 'congress',
        'url': 'https://www.politico.com',
    }

    FEED_URL = 'http://www.politico.com/rss/congress.xml'
