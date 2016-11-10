"""
PROJECT 3; CHALLENGE C:
BY: Hunter Charvat

CHALLENGE SPECIFICATIONS:
---------------------------------------------------------------------
Write a Python file that uploads an image to your Twitter account.
Make sure to use the hashtags #UMSI-206 #Proj3 in the tweet.

Requirements:
1) Write a Python file that uploads an image to your Twitter account.
2) Make sure to use the hashtags #UMSI-206 #Proj3 in the tweet.

Deliverables:
1) You will demo this live for grading.
---------------------------------------------------------------------

CITATIONS:
---------------------------------------------------------------------
(1): Sackoverflow user Brobin
        - How to use api.update_with_media()
        - http://stackoverflow.com/questions/31748444/how-to-update-twitter-status-with-image-using-image-url-in-tweepy
(2): Python Documentation by Python Software Foundation
        - How to use configparser to retrieve data from file
        - https://docs.python.org/3/library/configparser.html
---------------------------------------------------------------------
"""

import configparser
import tweepy
import requests

# Store personal info in untracked file and get it
config = configparser.ConfigParser()
config.read('config.ini')
inf = config['twitter_info']
AT = inf['at']
ATS = inf['ats']
CK = inf['ck']
CS = inf['cs']

FNAME = 'deadmau5_2016.jpg'
MESSAGE = "Can't wait for the 2016 album. #USMI-206 #Proj3"

# Create an instance of tweepy twitter API
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)


api.update_with_media(FNAME, MESSAGE)
