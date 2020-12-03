from . import views
from django.urls import path

urlpatterns = [
    # this url
    path('', views.newyear, name="newyear"),
    path('extending', views.extending, name="extending")
]