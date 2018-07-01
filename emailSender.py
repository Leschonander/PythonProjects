import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from getpass import getpass
from pyfiglet import figlet_format

print(figlet_format('Your Python Email Sender Client!', font ='big'))

contacts = {
    "John Doe": 'john@gmail.com',
    "John Smith": 'Smith@optonline.net'
}

login = str(input("Do you want to login? "))
if login == "Yes":
    me = str(input("Input your email: "))
    password = getpass()
else:
    print(figlet_format('Bye!', font ='big'))
    exit()
#me = str(input("Input your email: "))
#password = getpass()
def service():    
    query = str(input("What do you want to do? Send a email or look at your contacts? Or would you want to end the service? "))
    if query == "Email":
        you = str(input("Input email of recipient: "))
        msg = str(input("Input body of Email: "))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(me, password)
        
        server.sendmail(me, you, msg)
        server.quit()

        service()
    elif query == "Contacts":
        print(contacts)
        service()
    elif query == "End":
        print(figlet_format('Bye!', font ='big'))
        exit()

if login == "Yes":
    service()


# msg['Subject'] = input("Input subject: ")

