from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Counter1', views.index1),
    path('Counter2', views.index2),

]