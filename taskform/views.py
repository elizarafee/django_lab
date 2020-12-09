from django.shortcuts import render
from django import forms

class NewTaskForm(forms.Form):
    taskname = forms.CharField(label="Task Name")
    priority = forms.IntegerField(label="Priority", max_value=10, min_value=2)

# Create your views here.
def mainform(request):
    return render(request, "taskform/dataform.html", {
        "task" : NewTaskForm()
    })

def tasks(request):
    return render(request, "taskform/tasks.html")