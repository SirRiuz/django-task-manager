
# Django 
from django.db import models

# Models
from accounts.models import User


class Task(models.Model):

    """
     Este modelo se encarga de gestionar
     todas las tareas
    """
    user = models.ForeignKey(to=User , on_delete=models.CASCADE , unique=False)

    title = models.CharField(
        null=False,default='',
        max_length=100,
        help_text='Titulo de la tarea'
    )

    description = models.TextField(
        blank=True,
        null=True,
        default='',
        help_text='Descripcion de la tarea'
    )

    taskStatus = models.CharField(
        default='nan',
        max_length=100,
        null=False,
        help_text='Estado de la tarea'
    )
    
    isComplete = models.BooleanField(default=False)
    taskExpire = models.DateField(null=False , help_text='Fecha de expiracion de la tarea')
    taskCreated = models.DateField(auto_now=True , help_text='Fecha de creacion de la tarea')
    
    def __str__(self):
        return self.title

