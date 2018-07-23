from flask_mail import Message
from flask import render_template
from app import mail
#I did the config for email earlier I am pretty sure...


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

def sendSuggestion(form):
    send_email('New Coffee Place Suggestion',
    sender= form.email.data,
    recipients='leschonander@gmail.com',
    text_body=render_template('mail.txt',
        form=form),
    html_body=render_template('mail.html',
        form=form))