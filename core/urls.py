
from django.contrib import admin
from django.urls import path
from .views import homePage
from task.views import TaskManager

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', TaskManager.as_view()),
]
