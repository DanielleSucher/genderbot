import json
import os
from twitter import *


class TwitterBot:
  def __init__(self, app_name):
    self.app_name = app_name
    self.__read_credentials_files()
    self.__sign_in_with_oauth()

  def post_tweet(self, message):
    self.twitter.statuses.update(status=message)

  def __read_credentials_files(self):
    self.bot_creds = os.path.join(os.path.dirname(__file__), ".bot_credentials")
    env_filepath = os.path.join(os.path.dirname(__file__), ".env")
    env_file = open(env_filepath, 'r')
    env_data = json.load(env_file)
    self.consumer_key = str(env_data['CONSUMER_KEY'])
    self.consumer_secret = str(env_data['CONSUMER_SECRET'])
    env_file.close()

  def __sign_in_with_oauth(self):
    if not os.path.exists(self.bot_creds):
      oauth_dance(self.app_name, self.consumer_key, self.consumer_secret, self.bot_creds)

    oauth_token, oauth_secret = read_token_file(self.bot_creds)
    self.twitter = Twitter(auth=OAuth(
      oauth_token, oauth_secret, self.consumer_key, self.consumer_secret))

