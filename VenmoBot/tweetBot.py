from cred import *
from time import sleep
import tweepy


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

File = open('transactions.txt', 'r')
fileLines = File.readlines()
File.close()


def tweet():
    for line in fileLines:
        try:
            print(line)
            if line != '\n': #Skip blank lines...
                api.update_status(line)
                sleep(900) #15 mins...
        else:
            pass
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(5)
# tweet()