from django.urls import path
from . import views

app_name = "taskform"

urlpatterns = [
    path("", views.tasks, name = "tasks"),
    path("mainform", views.mainform, name = "mainform")
]