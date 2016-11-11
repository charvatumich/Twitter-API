# """
# PROJECT 3; CHALLENGE D:
# BY: Hunter Charvat
#
# CHALLENGE SPECIFICATIONS:
# ---------------------------------------------------------------------
# In this assignment you must do a Twitter search on any term of your choice.
# Be prepared to change the search term during demo.
#
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results
# ---------------------------------------------------------------------
#
# CITATIONS:
# ---------------------------------------------------------------------
# (1): Stackoverflow user Martijn Pieters
#         - How to print without spaces between values
#         - http://stackoverflow.com/questions/28669459/how-to-print-variables-without-spaces-between-values
# ---------------------------------------------------------------------
# """

import configparser
import tweepy
import nltk
from textblob import TextBlob


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

results = api.search(q=SEARCH)
c = 1
for tweet in results:
    print(str(c) + ')')
    print(tweet.text)
    print('*****')
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment, '\n')
    c += 1