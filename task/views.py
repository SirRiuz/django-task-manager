
# Django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Models 
from .models import Task


@login_required
def createTask(request):
    if request.method == 'POST':
        print('post')
    
    return render(
        request,
        template_name='create_task.html'
    )