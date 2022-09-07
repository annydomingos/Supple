from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.

class UsuarioManager(BaseUserManager):
  use_in_migrations = True

  def _create_user(self, email, first_name, password, **extra_fields):
    if not email:
      raise ValueError('O email é obrigatório')
    email = self.normalize_email(email)
    user = self.model(email = email, first_name = first_name, username = email, **extra_fields)

    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, first_name, password, **extra_fields):
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)
    return self._create_user(email, first_name, password, **extra_fields)

  def create_superuser(self, email, first_name, password, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    if extra_fields.get('is_staff') is not True:
      raise ValueError('Para criar superusuario "is_staff" precisa ser True')
    if extra_fields.get('is_superuser') is not True:
      raise ValueError('Para criar superusuario "is_superuser" precisa ser True')
    return self._create_user(email, first_name, password, **extra_fields)


class Usuario(AbstractUser):
  email = models.EmailField('Email', unique=True)
  first_name = models.CharField('Nome', max_length=50)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['password']


  objects = UsuarioManager()

  class Meta:
    verbose_name = 'Usuario'
    verbose_name_plural = 'Usuarios'
