from django.shortcuts import render
from django import forms

tasks = []

class NewTaskForm(forms.Form):
    taskname = forms.CharField(label="Task Name")
    # priority = forms.IntegerField(label="Priority", max_value=10, min_value=2)

# Create your views here.
def mainform(request):
    if request.method=="POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data("taskname")
            tasks.append(task)
            return render(request, "taskform/tasks.html")
        else:
            return render(request, "taskform/tasks.html", {
                "form" : form
            })

    return render(request, "taskform/dataform.html", {
        "form" : NewTaskForm()
    })

def tasks(request, tasks):
    return render(request, "taskform/tasks.html", {
        "tasks" : tasks
    })