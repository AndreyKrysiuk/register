from django.shortcuts import render, redirect

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
    i = 0
    persons = get_all_persons()
    checking_d = get_all_checking()
    checking_p = get_all_checking()

    if request.method == "POST":
        name = request.POST['name']
        category = request.POST['category']
        job = request.POST['job']
        position = request.POST['position']
        region = request.POST['region']
        isPretender = request.POST['isPretender']
        solution = request.POST['solution']
        date_accept_ban = request.POST['date_accept_ban']
        date_refuse_ban = request.POST['date_refuse_ban']
        resolution = request.POST['resolution']

        add_new_checking( add_new_person(name, category, job, position, region, isPretender), solution,resolution,date_accept_ban,date_refuse_ban)

    return render(request, 'admin_checking.html', locals())


def admin_checking_delete(request, id):
    delete_checking(id)
    return redirect("/admin_checking")


def admin_checking_update(request, id):
    name = request.POST['name']
    category = request.POST['category']
    job = request.POST['job']
    position = request.POST['position']
    region = request.POST['region']
    isPretender = request.POST['isPretender']
    solution = request.POST['solution']
    date_accept_ban = request.POST['date_accept_ban']
    date_refuse_ban = request.POST['date_refuse_ban']
    resolution = request.POST['resolution']

    update_checking_with_person(id, name, category, job, position, region, solution, resolution, date_refuse_ban, date_accept_ban, isPretender)

    update_checking(id,solution,resolution,date_refuse_ban,date_accept_ban)
    return redirect("/admin_checking")



