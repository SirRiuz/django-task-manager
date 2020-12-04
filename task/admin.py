
# Django
from django.contrib import admin

# Models
from .models import Task

@admin.register(Task)
class TackAdmin(admin.ModelAdmin):
    pass



