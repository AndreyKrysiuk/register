"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from Project.views import Userviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', Userviews.home),
    url(r'^$', Userviews.home),
    url(r'^banished/$', Userviews.banished),
    url(r'^checking/$', Userviews.checking),
    url(r'^contact/$', Userviews.contact),
    url(r'^court_proceedings/$', Userviews.court_proceedings),
    url(r'^documents/$', Userviews.documents),
    url(r'^question/$', Userviews.question),
    url(r'^address/$', Userviews.address),
    url(r'^work_material/$', Userviews.work_material),
    url(r'^work_material_links/$', Userviews.work_material_links),
    url(r'^data/$', Userviews.data_about_checking),
    url(r'^public_council/$', Userviews.public_council),
    url(r'^public_council_links/$', Userviews.public_council_links),
    url(r'^register/$', Userviews.register)

]
