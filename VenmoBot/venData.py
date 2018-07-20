import requests as re
import json
from time import sleep

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

example()
write()
anonWrite()
