
# Django
from django.db import models
from django.contrib.auth.models import (BaseUserManager,PermissionsMixin,AbstractBaseUser)




class User(AbstractBaseUser , PermissionsMixin):

    """
     Este modelo se encarga de administrar
     todo los datos de lo usuarios
    """
    
    objects = ''

    userName = models.CharField(
        max_length=120,
        null=False,
        default='',
        help_text='Nombre de usuario'
    )

    nickName = models.CharField(
        null=False,
        max_length=50,
        unique=True,
        help_text='Nick name'
    )
    
    email = models.EmailField(null=False,unique=True,help_text='Correo electronico')
    phoneNumber = models.IntegerField(null=True,blank=True,help_text='Numero de telefono')

    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


    USERNAME_FIELD = 'nickName'
    REQUIRED_FIELDS = [  ]


    def __str__(self):
        return self.nickName









