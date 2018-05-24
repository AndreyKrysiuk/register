from django.shortcuts import render
from django.http import HttpResponseRedirect

from register.Schemas.User import *
from register.Schemas.Checking import *
from register.Schemas.Register import *
from register.Schemas.Person import *


def home(request):
    return render(request, 'register.html')


def address(request):
    return render(request, 'address.html')


def contact(request):
    return render(request, 'contact.html')


def banished(request):
    return render(request, 'banished.html')


def checking(request):
    return render(request, 'checking.html')


def contact(request):
    return render(request, 'contact.html')


def court_proceedings(request):
    return render(request, 'court_proceedings.html')


def documents(request):
    return render(request, 'documents.html')


def question(request):
    return render(request, 'question.html')


def work_material(request):
    return render(request, 'work_material.html')


def work_material_links(request):
    return render(request, 'work_material_links.html')


def data_about_checking(request):
    return render(request, 'data_about_checking.html')


def public_council(request):
    return render(request, 'public_council.html')


def public_council_links(request):
    return render(request, 'public_council_links.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)

        return render(request, 'register.html')


def admin_checking(request):

    persons = get_all_persons()
    checking_d = get_all_checking()
    checking_p = get_all_checking()




    return render(request, 'admin_checking.html', locals())