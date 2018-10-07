import json
import tweepy 
from tweepy import Stream
from tweepy.streaming import StreamListener
from creds import *
from markdown2 import markdown
import os
from jinja2 import Environment, PackageLoader

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

'''
for status in tweepy.Cursor(api.user_timeline, screen_name='@jongold').items(20): #This will get all the persons tweets
    print(status._json['text']) # @realDonaldTrump
'''

# stopWords = ['RT']
# myTweets = [word for word in myTweets if word not in stopWords]

def writeTweets(username, amount):
    '''Write Tweets to a Markdown file.'''
    myTweets = []
    for status in tweepy.Cursor(api.user_timeline, screen_name=username).items(amount):
        myTweets.append(status.text)
    # print(myTweets)
    words = open('tweets.md', 'w', encoding="utf-8")
    for text in myTweets:
        words.write(text + '\n' + '\n')

# writeTweets('@LarsESchonander', 30)

def tweetTemplate():
    '''Write Tweets to styled HTML page with Jinja templates'''
    tweetMarkDown = 'tweets.md'
    with open(tweetMarkDown, 'r', encoding="utf-8") as file:
        parsed_md = markdown(file.read()) #Emoji problem
    
    env = Environment(loader=PackageLoader('client', 'templates'))
    tweet_template = env.get_template('tweetBlog.html')

    data = {
        'content': parsed_md
    }
    
    tweet_html_content = tweet_template.render(posts = data)
    with open('output/tweetPost.html', 'w', encoding="utf-8") as file:
        file.write(tweet_html_content)

# tweetTemplate()

'''Normally would do imports above but seperating concerns! '''

import smtplib
import email.message

def sendEmail(): # for loop over the function, actually!
    '''Send Tweets as an email...'''
    server = smtplib.SMTP('smtp.gmail.com:587')

    with open('output/tweetPost.html', 'r', encoding="utf-8") as file:
            emailContent = (file.read()) #Emoji problem

    # for mass email is would be a for loop, looping over a list of emails...
    msg = email.message.Message()
    msg['Subject'] = 'Your Weekly Tweets'
    
    
    msg['From'] = ''
    msg['To'] = ''
    password = ""
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(emailContent)
    
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    
    s.sendmail(msg['From'], [msg['To']], str(msg).encode('utf-8'))

# sendEmail()