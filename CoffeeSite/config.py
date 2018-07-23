import os


class Config(object):
    SECRET_KEY = os.environ.get('NOT_SECRET_KEY') or 'NOT THE KEY IN PRODUCTION CODE'#You thought you would get the key wouldn't you?