import random
import re
from twitterbot import TwitterBot
import wikipedia


class Genderbot(TwitterBot):

  def tweet(self):
    article = self.__random_wikipedia_article()
    match = re.search(r"\bis [^.?]+", article.content, re.UNICODE)
    if match:
      status = self.__format_status(match.group(0), article.url)
      self.post_tweet(status)

  def __format_status(self, is_phrase, url):
    status = 'gender %s' % (is_phrase)
    if len(status) > 114: status = status[0:113] + '...'
    return status + ' %s' % (url)

  def __random_wikipedia_article(self):
    random_title = wikipedia.random(pages=1)
    return wikipedia.page(title=random_title)


if __name__ == "__main__":
  try:
    Genderbot("CustomGender").tweet()
  except:
    pass
