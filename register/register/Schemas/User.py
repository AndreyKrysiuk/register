from mongoengine import *


class User(Document):
    login = StringField(max_length=60, required=True, min_length=10)
    password = StringField(max_length=120, required=True)
    isBanned = BooleanField(required=True)
    isAdmin = BooleanField(required=True)


def addNewUser(login, password, isBanned = False, isAdmin = False):
    mongo_path = "mongodb://admin:avemaria@ds131800.mlab.com:31800/register"
    connect(
        db='register',
        username='admin',
        password='avemaria',
        host = mongo_path)

    user = User()
    user.login = login
    user.password = password
    user.isBanned = isBanned
    user.isAdmin = isAdmin
    user.save()
