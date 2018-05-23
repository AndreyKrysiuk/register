from mongoengine import *


class User(Document):
    login = StringField(max_length=30, required=True, min_length=6)
    password = StringField(max_length=30, required=True, min_length=9)
    isBanned = BooleanField(required=True)
    isAdmin = BooleanField(required=True)


def add_new_user(login, password, is_banned = False, is_admin = False):
    user = User()
    if (len(login) >= 6) and (len(login) <= 30):
        user.login = login
    else:
        return -1

    if (len(password) >= 9) and (len(login) <= 30):
        user.password = password
    else:
        return -2

    user.isBanned = is_banned
    user.isAdmin = is_admin

    user.save()