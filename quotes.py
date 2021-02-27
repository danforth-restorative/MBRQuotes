# Tweet Quotes from Yaml
# Adapted from: https://dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, yaml, random, os

# Get environment variables (stored encrypted in github repository, and called into the OS from the action workflow file main.yml)
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_KEY = os.environ.get('ACCESS_KEY')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

sourceLabel = 'MBR Quotes'

with open('quotes.yaml','r') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    quotes = yaml.load(file, Loader=yaml.FullLoader)
    item = random.choice(quotes)
    print(item)
    api.update_status(status=item, source=sourceLabel)
    file.close()

with open('quotes.yaml') as og, open("tmp", "w") as dest:
    for line in og:
        decoded_string = bytes(line, "utf-8").decode("unicode_escape") 
        if item not in decoded_string:
            dest.write(line)
os.rename("tmp", "quotes.yaml")
