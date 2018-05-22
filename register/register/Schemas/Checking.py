from mongoengine import *
from register.Schemas import Person


class Checking(Document):
    person_id = ReferenceField(Person)
    solution = StringField(max_length=240)
    date_accept_ban = DateTimeField()
    date_refuse_ban = DateTimeField()
    resolution = StringField(max_length=240)
    copy_of_request = StringField(max_length=150)
    copy_of_declaration = StringField(max_length=150)

