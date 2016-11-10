"""
PROJECT 3; CHALLENGE D:
BY: Hunter Charvat

CHALLENGE SPECIFICATIONS:
---------------------------------------------------------------------
In this assignment you must do a Twitter search on any term of your choice.
Be prepared to change the search term during demo.

Deliverables:
1) Print each tweet
2) Print the average subjectivity of the results
3) Print the average polarity of the results
---------------------------------------------------------------------

CITATIONS:
---------------------------------------------------------------------
(1):
        -
        -
---------------------------------------------------------------------
"""

import configparser
import tweepy

# Store personal info in untracked file and get it
config = configparser.ConfigParser()
config.read('config.ini')
inf = config['twitter_info']
AT = inf['at']
ATS = inf['ats']
CK = inf['ck']
CS = inf['cs']

SEARCH = "Love"

# Create an instance of tweepy twitter API
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)

results = api.search(q=SEARCH, rpp=100)
for tweet in results:
    tweet[]