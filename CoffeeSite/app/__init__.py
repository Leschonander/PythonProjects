from flask import Flask
from config import Config
from flask_mail import Mail, Message
#yeah you do mail here...
#Guide here https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-email-support
app = Flask(__name__)
#mail stuff

mail = Mail(app)

app.static_folder = 'static'
app.config.from_object(Config)#from config.py . Config

from app import routes
# from app import myForm
