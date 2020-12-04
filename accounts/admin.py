
# Django
from django.contrib import admin

#Models 
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

# Register your models here.
