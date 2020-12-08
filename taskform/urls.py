from django.urls import path
from . import views

app_name = "taskform"

urlpatterns = [
    path("", views.mainform, name = "mainform")
]