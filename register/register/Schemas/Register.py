from mongoengine import *
from register.Schemas import Person


class Register(Document):
    person_id = ReferenceField('Person')
    result = StringField(max_length=240)
    ban_time = StringField(max_length=90)






