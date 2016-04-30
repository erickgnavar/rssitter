# coding: utf-8
from __future__ import unicode_literals
import os
import time

from twython import Twython
import feedparser


APP_KEY = os.environ.get('APP_KEY')
APP_SECRET = os.environ.get('APP_SECRET')
OAUTH_TOKEN = os.environ.get('OAUTH_TOKEN')
OAUTH_TOKEN_SECRET = os.environ.get('OAUTH_TOKEN_SECRET')
FEED_URL = os.environ.get('FEED_URL')

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


def post_tweet(entry):
    template = """
{title}
{tags}
{link}
    """
    entry['tags'] = ' '.join(map(lambda x: '#{}'.format(x['term']), entry.get('tags', [])))
    twitter.update_status(status=template.format(**entry))


def main():
    feed = feedparser.parse(FEED_URL)
    for entry in feed['entries']:
        post_tweet(entry)
        time.sleep(10)


if __name__ == '__main__':
    main()
