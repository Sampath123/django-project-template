#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from todoapp.models import Task, User
#from django.contrib.auth.models import User


def index1(request):
    return HttpResponse("Hello")


def get_all_tasks(request):
    all_task = Task.objects.all()
    return render(request, "tasks.html", {"tasks": all_task,
                                          "title": "All Tasks"})


def get_private_tasks(request):
    private_task = Task.objects.filter(task_visibility=1)
    return render(request, "tasks.html", {"tasks": private_task,
                                           "title": "Private Tasks"})


def get_public_tasks(request):
    public_task = Task.objects.filter(task_visibility=0)
    return render(request, "tasks.html", {"tasks": public_task,
                                           "title": "Public Tasks"})


def get_user_tasks(request, name):
    user = User.objects.get(username=name)
    user_task = Task.objects.filter(user_name=user.id)
    return render(request, "tasks.html", {"tasks": user_task,
                            "users": user.username, "title": "User Tasks"})
