
# Django 
from django.contrib.auth.decorators import login_required
from django.shortcuts import (redirect,render)

# Models
from task.models import Task

@login_required
def homePage(request):
    tasks = Task.objects.filter(user = request.user)
    return render(
        request,
        template_name='home.html',
        context={
            'tasks':tasks
        }
    )