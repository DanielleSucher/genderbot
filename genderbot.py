import json
import os
import random
import re
import sys
from twitter import *
import wikipedia

if random.randrange(2) == 0: sys.exit(0)

MY_TWITTER_CREDS = os.path.join(os.path.dirname(__file__), ".genderbot_credentials")

env_filepath = os.path.join(os.path.dirname(__file__), ".env")
env_file = open(env_filepath, 'r')
env_data = json.load(env_file)
CONSUMER_KEY = str(env_data['CONSUMER_KEY'])
CONSUMER_SECRET = str(env_data['CONSUMER_SECRET'])
env_file.close()

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
  match = re.search(unicode(r"\bis [^.?]+"), random_article.content, re.UNICODE)
  if match:
    status = 'gender %s' % (match.group(0))
    if len(status) > 114: status = status[0:113] + '...'
    status += ' %s' % (random_article.url)
    twitter.statuses.update(status=status)
except:
  pass
