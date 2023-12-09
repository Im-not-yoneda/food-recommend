from django.urls import path

from . import views

urlpatterns = [
    path("", views.foodrecommend, name="recommend"),
    path("about/", views.about, name="about"),
    path("insert/", views.insertFood, name="insert"),
    path("result/", views.foodrecommend, name="result")
]