from sources import generic_feed

SOURCE = {
    'name': 'Reuters (US News)',
    'url': 'https://www.reuters.com',
}

FEED_URL = 'http://feeds.reuters.com/Reuters/domesticNews'

update = generic_feed.create_update(FEED_URL, SOURCE)