import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from getpass import getpass
from pyfiglet import figlet_format
import sqlite3
import sys
import email
import imaplib

#Setup
sqlite_file = 'emaildb.sqlite' #The database

conn = sqlite3.connect(sqlite_file) #The connection
c = conn.cursor()
M = imaplib.IMAP4_SSL('imap.gmail.com')

print(figlet_format('Your Python Email Sender Client!', font ='big'))
#SQL Commands

# Add Email
def addEmail():
    idA = int(input("Input the numeric id of the person"))
    name = str(input("Input the name of the person: "))
    email = str((input("Input the email of the person: ")))

    c.execute('''INSERT INTO emails(id,name,email)
            VALUES(?,?,?)''',(idA,name,email)
    )
#Update by to add ID
def updateID(): #Update info example
    id1 = int(input("Input ID of what to update: "))
    name = str(input("Input name of person you want to update: "))
    c.execute('''UPDATE emails SET id = ? WHERE name = ? ''',
    (id1,name))
#Look at all contacts
def lookAtAllRows():
    for row in c.execute('''SELECT * FROM emails ORDER BY id '''):
        print(row)
#Delete a person
def deletePerson(): #Delete a person based on the name provided
    name = str(input("Input the name of the person you want to remove: "))
    c.execute('''DELETE FROM emails WHERE name = ? ''',
    (name,))
#The quit end
def quit():
    print(figlet_format('Bye!', font ='big'))
    exit()
#Imapstuff


#The actual client

def service():
    query = str(input("Send an email, look at your contacts or ones inbox? Or quit the service? "))
    if query == "Contacts":
        contactOption = str(input("Add, Update, or Delete? "))
        if contactOption == "Add":
            addEmail()
            service()
        elif contactOption == "Update":
            #Add a update by ID/Name/Email option
            #For now just add the ID
            updateID()
            service()
        elif contactOption == "Delete":
            deletePerson()
            service()
        else:
            service()
    elif query == "Email":
        user_id = int(input("Input ID of what to look at: "))
        c.execute('''SELECT name, email FROM emails WHERE id = ? ''',
            (user_id,))
        recipient = c.fetchone()
        you = recipient[1]
        body = str(input("Input the body of the message: "))

        headlineFileWrite = open('headlines.txt', 'w')
        headlineFileWrite.write(body)
        headlineFileWrite.close()

        with open('headlines.txt') as fp:
            msg = MIMEText(fp.read())

        msg['Subject'] = str(input("Input Subject header of Email: "))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(me, password)
        
        server.sendmail(me, you, str(msg))
        server.quit()
        service()
    elif query == "Quit":
        quit()
    else:
        print("Input a actual command please.")
        service()
#Login


# M = imaplib.IMAP4_SSL('imap.gmail.com') Is above but for refernce
#
login = str(input("Do you want to login? "))
if login == "Yes":
    me = str(input("Input your email: "))
    password = getpass()
    M.login(me, password)
    service()
else:
    quit()