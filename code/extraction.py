#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os
import tweepy
import csv

# Twitter credentials
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

# Authorize tweetpy client
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Get all twitts with query term
term = "#PrayForParis"
language = "es"
elements = 5000

import re
def simple_preprocess(in_txt):
    # Remove new lines
    in_txt = item.text.strip().replace('\n', '')
    # Remove hyperlinks
    text = re.sub(r"http\S+", "", in_txt)
    return text

twitts = []
i = 0
try:
    for item in tweepy.Cursor(api.search, q=term, lang=language).items(elements):
        twitt = [item.user.screen_name, simple_preprocess(item.text).encode('utf8')]
        print i, twitt[1]
        i+=1
        twitts.append(twitt)
except KeyboardInterrupt:
    print "Stop getting twitts..."

print("-----------------------")
print("twiitts:%s" % len(twitts))
print("-----------------------")

# Write twitts to CSV file
with open('twitts.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for twitt in twitts:
        spamwriter.writerow(twitt)
