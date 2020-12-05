
from django.contrib import admin
from django.urls import path
from .views import (homePage,basePage)
from task.views import createTask

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/task/', createTask),
    path('home/', homePage),
    path('', basePage),
]
