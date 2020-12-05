

# django 
from django import forms


class TaskForm(forms.Form):

    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=1000)
    user = forms.CharField(max_length=100)
    taskExpire = forms.DateField()

