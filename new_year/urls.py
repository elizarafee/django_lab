from . import views
from django.urls import path

app_name = "new_year"
urlpatterns = [
    # this url
    path('', views.newyear, name="newyear"),
    path('extending', views.extending, name="extending")
]