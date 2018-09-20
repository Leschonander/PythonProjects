from figmaClass import figmaAPIComments
import boto3
from typing import Dict

client = boto3.client('sns')

token = {'X-FIGMA-TOKEN': 'Insert key here'}
filename = "insert file here"
testComment = figmaAPIComments(token)
# print(testComment.getComments(filename))
comments = (testComment.getComments(filename))

def sms(comment: str):
        client.publish(
            PhoneNumber = " insert phone number here",
            Message = comment
    )
words = []
length = (len(comments['comments']))
print(comments['comments'][1]['message'])
for i in range(0, length):
    elem = comments['comments'][i]['message']
    words.append(elem)

'''
for i in words:
    sms(i)
'''