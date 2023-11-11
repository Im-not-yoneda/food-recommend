from django.urls import path

from . import views

urlpatterns = [
    path("", views.homework, name="napsac"),
    path("test/", views.index, name="index"),
]