from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from register.Schemas.Checking import *
from register.Schemas.Register import *
from register.Schemas.Person import *


def home(request):
    return redirect("/register")


def address(request):
    return render(request, 'address.html')


def contact(request):
    return render(request, 'contact.html')


def banished(request):
    return render(request, 'banished.html')


def checking(request):
    checking1 = get_all_checking()

    search = "none"
    is_search = False
    is_empty = True

    if request.method == "POST":
        _search = request.POST['search']

        checking1 = find_checking_by_person_name(_search)
        if checking1:
            is_empty = False
        is_search = True
        search = _search

    return render(request, 'checking.html', locals())


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

    register1 = get_all_register()
    search = "none"
    is_search = False
    is_empty = True

    if request.method == "POST":
        _search = request.POST['search']

        register1 = find_register_by_person_name(_search)
        if register1:
            is_empty = False
        is_search = True
        search = _search

    return render(request, 'register.html', locals())


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'register.html')
        else:
            print ("login error")
            return render(request, 'login.html')


def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']

        if password == password2:
            user = User.objects.create_user(username=username,
                                            password=username,
                                            email=email,
                                            first_name=firstname,
                                            last_name=lastname)
            user.is_staff = True
            user.save()
            return render(request, 'login.html')


def admin_checking(request):
    checking1 = get_all_checking()

    search = "none"
    is_search = False
    is_empty = True

    if request.method == "POST":
        _search = request.POST['search']

        checking1 = find_checking_by_person_name(_search)
        if checking1:
            is_empty = False
        is_search = True
        search = _search

    return render(request, 'admin_checking.html', locals())


def admin_checking_add(request):
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

        add_new_checking(add_new_person(name, category, job, position, region, isPretender), solution, resolution,
                         date_accept_ban, date_refuse_ban)
    return redirect("/admin_checking")


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


def admin_checking_move(request, id):
    result = request.POST['result']
    ban_time = request.POST['ban_time']
    move_checking(id, result, ban_time)
    return redirect("/admin_checking")


def admin_register(request):

    register1 = get_all_register()

    search = "none"
    is_search = False
    is_empty = True

    if request.method == "POST":
        _search = request.POST['search']

        register1 = find_register_by_person_name(_search)
        if register1:
            is_empty = False
        is_search = True
        search = _search

    return render(request, 'admin_register.html',locals())


def admin_register_add(request):

    if request.method == "POST":
        name = request.POST['name']
        category = request.POST['category']
        job = request.POST['job']
        position = request.POST['position']
        region = request.POST['region']
        isPretender = request.POST['isPretender']
        result = request.POST['result']
        ban_time = request.POST['ban_time']

        add_new_register(add_new_person(name, category, job, position, region, isPretender), result, ban_time)

    return redirect("/admin_register")


def admin_register_delete(request, id):
    delete_register(id)
    return redirect("/admin_register")


def admin_register_update(request, id):
    name = request.POST['name']
    category = request.POST['category']
    job = request.POST['job']
    position = request.POST['position']
    region = request.POST['region']
    isPretender = request.POST['isPretender']
    result = request.POST['result']
    ban_time = request.POST['ban_time']
    update_register_with_person(id,name,category,job,position,region,result,ban_time,isPretender)

    return redirect("/admin_register")


def admin_users(request):
    return render(request, 'admin_users.html')