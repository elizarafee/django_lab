from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def newyear(request):
    date = datetime.datetime.now()

    return render(request, "new_year/newyear.html", {
        "ans" : date.month == 1 and date.day == 1,
        "date" : date
    })