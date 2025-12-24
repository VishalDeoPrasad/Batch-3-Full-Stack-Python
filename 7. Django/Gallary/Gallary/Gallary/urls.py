from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.home),
    path("show_image/", views.show_image),
]
