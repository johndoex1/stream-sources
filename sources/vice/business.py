from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'VICE',
        'category': 'business',
        'url': 'https://www.vice.com',
    }

    FEED_URL = 'https://www.vice.com/en_us/rss/topic/business'
