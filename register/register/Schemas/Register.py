from mongoengine import *
from register.Schemas import Person


class Register(Document):
    person = ReferenceField('Person')
    result = StringField(max_length=240)
    ban_time = StringField(max_length=90)


def add_new_register(person, result='-', ban_time='-'):
    register = Register()

    exists = Register.objects(person_id=person, result=result, ban_time=ban_time)
    if exists is not None:
        return exists.id

    if person is None:
        return -1
    else:
        register.person = person

    if (result is None) or (len(result) > 240):
        return -1
    else:
        register.result = result

    if (ban_time is None) or (len(ban_time) > 90):
        return -1
    else:
        register.ban_time = ban_time

    register.save()


def get_register(this_id):
    register = Register.objects.get(this_id)
    if register is None:
        return -1
    else:
        return register


def get_all_register():
    return Register.objects()


def update_register(this_id, result, ban_time):
    if this_id is None:
        return -1

    register = Register.objects.get(this_id)
    if register is None:
        return -1

    if result is not None:
        register.update(**{"set__result" : result})

    if ban_time is not None:
        register.update(**{"set__ban_time" : ban_time})

    return 0


def delete_register(this_id):
    register = Register.objects(this_id = id)

    if register is not None:
        register.delete()
        return 0
    else:
        return -1


