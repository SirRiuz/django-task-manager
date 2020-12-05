
# Django
from django.shortcuts import (render,redirect)
from django.contrib.auth.decorators import (login_required)

# Models 
from .models import Task

# Forms 
from .taskForm import TaskForm

@login_required
def createTask(request):
    form = TaskForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            title = form.data['title']
            description = form.data['description']
            taskExpire = form.data['taskExpire']    

            newTask = Task.objects.create(
                user = request.user,
                title=title,
                description=description,
                taskExpire=taskExpire
            )
            print('Task created !!!')
        else:
            print(form.data)
            return render(
                request,
                template_name='error_create_task.html'
            )

    return redirect('/')