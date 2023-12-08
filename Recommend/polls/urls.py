from django.urls import path

from . import views

urlpatterns = [
    path("", views.homework, name="napsac"),
    path("insert/", views.insertFood, name="insert"),
    path("test/", views.index, name="index"),
]