from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about),
    path('services/', views.services),
    path('contact/', views.contact),
    path('gallary/', views.gallary)
]
