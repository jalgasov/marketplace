from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import auth_page

urlpatterns = [
    path('/', auth_page, name='auth_page'),
]
