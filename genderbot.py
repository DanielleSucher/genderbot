import os
import re
import wikipedia
from twitter import *

MY_TWITTER_CREDS = os.path.expanduser('./.genderbot_credentials')
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']

if not os.path.exists(MY_TWITTER_CREDS):
  oauth_dance("CustomGender", CONSUMER_KEY, CONSUMER_SECRET, MY_TWITTER_CREDS)

oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)
twitter = Twitter(auth=OAuth(
  oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

try:
  # Grab a random article from Wikipedia
  random_article_title = wikipedia.random(pages=1)
  random_article = wikipedia.page(title=random_article_title)

  # If it has an "is..." string, set the definition of gender and tweet about it.
  match = re.search(unicode("is [^\.\?]+"), random_article.content, re.UNICODE)
  if match:
    status = 'gender %s' % (match.group(0))
    if len(status) > 114: status = status[0:113] + '...'
    status += ' %s' % (random_article.url)
    twitter.statuses.update(status=status)
except:
  pass
