from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.core.validators import MinLengthValidator
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self, username, password, **extra_fields):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError(_('Username should be provided'))
        
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        """
        Creates and saves a superuser with the given username and password.
        """
        extra_fields.setdefault("is_staff", True)      # Grants access to admin site
        extra_fields.setdefault("is_superuser", True)  # Provides all superuser permissions
        extra_fields.setdefault("is_active", True)     # use is_active = False instead of deleting accounts

        if not extra_fields.get('is_staff'):
            raise ValueError(_("Superusers must have is_staff = True"))

        if not extra_fields.get('is_superuser'):
            raise ValueError(_("Superusers must have is_superuser = True"))

        if not extra_fields.get('is_active'):
            raise ValueError(_("Superusers must have is_active = True"))

        return self.create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id_user = models.BigAutoField(primary_key=True)
    username = models.CharField(
        'Username', validators=[MinLengthValidator(5)], max_length=20, 
        unique=True, help_text="Username must contain between 5 and 20 characters")
    first_name = models.CharField("Name", max_length=30)
    last_name = models.CharField("Last_Name", max_length=30)
    password = models.CharField('Password', max_length=256)
    email = models.EmailField('Email', max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True, blank=True)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email"]
   
    def save(self, **kwargs):
        if not self.is_staff:
            self.password = make_password(self.password)
        super().save(**kwargs)

    def __str__(self):
        return "Username: {}, Email: {}".format(
            self.username, self.email)

