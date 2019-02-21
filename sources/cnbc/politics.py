from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'CNBC (Politics)',
        'url': 'https://www.cnbc.com',
    }

    FEED_URL = 'https://www.cnbc.com/id/10000113/device/rss/rss.html'
