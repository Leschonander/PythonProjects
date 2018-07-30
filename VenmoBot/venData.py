import requests as re
import json
from time import sleep
import pandas as pd

venmoData = re.get('https://venmo.com/api/v5/public?limit=100')
venmoDataJSON = venmoData.json()

# print(venmoDataJSON)
# print(venmoDataJSON['data'])

def example():  
    for i in range(0,10):
        print("Sender: ",venmoDataJSON['data'][i]['actor']['name'])
        print("Message: ",venmoDataJSON['data'][i]["message"])
        print("Recipient: ",venmoDataJSON['data'][i]["transactions"][0]["target"]['name'])
        # sleep(5)


def write():
    headlineFileWrite = open('transactions.md', 'w', encoding="utf-8")
    # maxScrape = int(input("How many people have their venmo taken today? "))
    for i in range(0,50):
        headlineFileWrite.write(
            "Sender: " + venmoDataJSON['data'][i]['actor']['name'] + " " +
            "Recipient: " + venmoDataJSON['data'][i]["transactions"][0]["target"]['name'] + " " +
            "Message: " + venmoDataJSON['data'][i]["message"] + " " + 
            "Date Created: " + venmoDataJSON['data'][i]["transactions"][0]["target"]['date_created'] + " " + "\n"
            

        )
    
    headlineFileWrite.close()
def anonWrite():
    headlineFileWrite = open('AnonTransactions.md', 'w', encoding="utf-8")
    # maxScrape = int(input("How many people have their venmo taken today? "))
    for i in range(0,10):
        headlineFileWrite.write(
            "Message: " + venmoDataJSON['data'][i]["message"] + " " + 
            "Date Created: " + venmoDataJSON['data'][i]["transactions"][0]["target"]['date_created'] + " " + "\n"
        )
    
    headlineFileWrite.close()

def venmoDataCsv():
    # Test series of data...
    message = pd.Series(venmoDataJSON["data"][0]["message"])
        # print(message)

    name = pd.Series(venmoDataJSON['data'][0]['actor']['name'])
        # print(name)

    recipientName = pd.Series(venmoDataJSON['data'][0]["transactions"][0]["target"]['name'])
        # print(recipientName)

    date = pd.Series(venmoDataJSON['data'][0]["transactions"][0]["target"]['date_created'])
        # print(date)

    showCaseDF = pd.DataFrame({
        'Sender': name,
        'Recipient': recipientName,
        'Message': message,
        'Date Created': date
        })
    print(showCaseDF)

name = pd.Series(venmoDataJSON['data'][0]['actor']['name'])
msg = pd.Series(venmoDataJSON["data"][0]["message"])
recipient = pd.Series(venmoDataJSON['data'][0]["transactions"][0]["target"]['name'])
date = pd.Series(venmoDataJSON['data'][0]["transactions"][0]["target"]['date_created'])
for i in range(1,50):
    name[i] = venmoDataJSON['data'][i]['actor']['name']
    msg[i] = venmoDataJSON["data"][i]["message"]
    recipient[i] = venmoDataJSON['data'][i]["transactions"][0]["target"]['name']
    date[i] = venmoDataJSON['data'][i]["transactions"][0]["target"]['date_created']

df = pd.DataFrame({
    'Name': name,
    'Date': date,
    'Recipient': recipient,
    'Message': msg
})
# print(df)    
    
example()
write()
anonWrite()
venmoDataCsv()
