from mongoengine import *


class User(Document):
    login = StringField(max_length=60, required=True, min_length=10)
    password = StringField(max_length=120, required=True)
    isBanned = BooleanField(required=True)
    isAdmin = BooleanField(required=True)