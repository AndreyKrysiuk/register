from mongoengine import *


class Person(Document):
    name = StringField(required=True, max_length=60)
    category = StringField(max_length=120)
    job = StringField(max_length=120)
    position = StringField(max_length=120)
    region = StringField(max_length=60)
    isPretender = BooleanField(required=True)



def update_person(id, name, category, job, position, region, isPretender):
    person = Person.objects(id=id)[0]
    if person is None:
        return -1

    person.update(**{"set__name": name})
    person.update(**{"set__category": category})
    person.update(**{"set__job": job})
    person.update(**{"set__position": position})
    person.update(**{"set__region": region})

    if isPretender is not None:
        person.update(**{"set__isPretender": isPretender})
    return 0


def delete_person(id):
    person = Person.objects(_id=id)
    if person is None:
        return -1
    else:
        person.delete()
        return 0


def get_person(id):
    person = Person.objects.get(id=id)
    if person is None:
        return -1
    else:
        return person[0]


def get_all_persons():
    return Person.objects()


def add_new_person(name, category, job, position, region, isPretender=False):
    person = Person()

    exists = Person.objects(name=name, category=category, job=job, position=position, region=region, isPretender=isPretender)

    if exists:
        return exists[0]

    person.name = name
    person.category = category
    person.job = job
    person.position = position
    person.region = region
    if isPretender is not None:
        person.isPretender = str2bool(isPretender)
    else:
        person.isPretender = False

    return person.save()


def update_person(id, name, category, job, position, region, isPretender=False):
    person = Person.objects(id=id)[0]
    if person is None:
        return -1

    if name is not None:
        person.update(**{"set__name": name})

    if category is not None:
        person.update(**{"set__category": category})

    if job is not None:
        person.update(**{"set__job": job})

    if position is not None:
        person.update(**{"set__position": position})

    if region is not None:
        person.update(**{"set__region": region})

    if isPretender is not None:
        person.update(**{"set__isPretender": str2bool(isPretender)})
    return 0


def delete_person(id):
    person = Person.objects(id=id)
    if person is None:
        return -1
    else:
        person.delete()
        return 0


def get_person(id):
    person = Person.objects(id=id)
    if person is None:
        return -1
    else:
        return person


def get_all_persons():
    return Person.objects()


def get_officials():
    return Person.objects(isPretender=False)


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1", "True")
