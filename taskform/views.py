from django.shortcuts import render

# Create your views here.
def mainform(request):
    return render(request, "taskform/dataform.html")