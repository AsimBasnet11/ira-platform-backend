from django.contrib import admin
from django.urls import path
from quizzes import views

urlpatterns = [
    path('', views.index),
]