"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from myfirstapp import views

urlpatterns = [
    url(r'^a$', views.hello, name="hola"),
    url(r'^bye/(.*)', views.adios, name="adios"),       #con el (.*) me coge lo que le pase como parametro, por ejemplo en ...:1234/bye/manolo me coge manolo
    url(r'^suma/(.*)$', views.sumador, name="suma"),
    url(r'^resta/(.*)$', views.restador, name="resta"),
    url(r'^multi/(.*)$', views.multiplicador, name="multiplicador"),
    url(r'^division/(.*)$', views.divisor, name="divisor"),
]

