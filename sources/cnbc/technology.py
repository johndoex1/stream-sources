from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'CNBC (Technology)',
        'url': 'https://www.cnbc.com',
    }

    FEED_URL = 'https://www.cnbc.com/id/19854910/device/rss/rss.html'
