from django.contrib import admin
from django.urls import include,path
from app import views

urlpatterns = [
    path("",views.index,name='home'),
    path("index",views.index,name='home'),
    path("about",views.about,name='about'),
    path("service",views.services,name='services'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
    path("contacts",views.contact,name='contact'),
    path("search", views.search, name='search'),
    path("search/res", views.search_res, name='search1'),
    path("filter", views.filter, name='filter'),
    path("filter/res", views.filter_res, name='filter1'),
    path("charts", views.charts, name='charts'),
    path("charts/res", views.charts_res, name='charts1')
]