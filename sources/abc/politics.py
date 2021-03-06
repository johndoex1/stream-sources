from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'ABC News',
        'category': 'politics',
        'url': 'https://abcnews.go.com/',
    }

    FEED_URL = 'https://abcnews.go.com/abcnews/politicsheadlines'
