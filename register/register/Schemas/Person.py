from mongoengine import *


class Person(Document):
    name = StringField(required=True, max_length=60)
    cathegory = StringField(max_length=120)
    job = StringField(max_length=120)
    position = StringField(max_length=120)
    region = StringField(max_length=60)
    isPretender = BooleanField(required=True)


