from django.urls import path
from . import views

app_name = "appli"
urlpatterns = [
    path("", views.index, name="index"), 
    path("show", views.show, name="show"),
    path("<str:name>", views.random, name="random")
]