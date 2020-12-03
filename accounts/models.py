
# Django
from django.db import models
from django.contrib.auth.models import (BaseUserManager,PermissionsMixin,AbstractBaseUser)


class CustomUserManager(BaseUserManager):
    
    """
     Este manager permite crear 
     usuarios normales y super 
     usuarios
    """

    def create_user(self , **kwargs) -> object:
        user = self.model(
            userName=kwargs['userName'],
            nickName=kwargs['nickName'],
            email=kwargs['email'],
            phoneNumber=kwargs['phoneNumber']
        )
        user.set_password(kwargs['password'])
        user.save(using=self._db)
        return user


    def create_superuser(self , **kwargs) -> object:
        user = self.create_user(**kwargs)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


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
    
    imageProfile = models.ImageField(
        upload_to='image' , 
        blank=True , 
        default='' , 
        help_text='Foto de perfil'
    )
    
    email = models.EmailField(null=False,unique=True,help_text='Correo electronico')
    phoneNumber = models.IntegerField(null=True,blank=True,help_text='Numero de telefono')

    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


    USERNAME_FIELD = 'nickName'
    REQUIRED_FIELDS = [ 'userName' , 'email' , 'password' , 'phoneNumber' ]


    def __str__(self):
        return self.nickName









