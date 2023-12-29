from django.urls import include,path

from . import views

urlpatterns = [
    path("", views.foodrecommend, name="recommend"),
    path("about/", views.about, name="about"),
    path("insert/", views.insertFood, name="insert"),
    path("result/", views.foodrecommend, name="result"),
    path("test/", views.test, name="test"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", views.signup, name="signup")
]