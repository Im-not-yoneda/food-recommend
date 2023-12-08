from django.urls import path

from . import views

urlpatterns = [
    path("", views.foodrecommend, name="knapsac"),
    path("about/", views.about, name="about"),
    path("insert/", views.insertFood, name="insert")
]