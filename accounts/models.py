from django.contrib.auth.password_validation import validate_password
from django.db import models

# Create your models here.
from django.contrib.auth.models import UserManager as DefaultUserManager, AbstractUser


class UserManager(DefaultUserManager):

    def _create_user(self, username, email, password, **extra_fields):
        user = self.model(username=username, email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return super()._create_user(username, email, password, **extra_fields)

    def create_user(self, username, email=None, password=None, first_name=None, last_name=None, **extra_fields):
        self._validate_credentials(username, email, password)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        self._validate_credentials(username, email, password)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(username, email, password, **extra_fields)

    def _validate_credentials(self, username, email, password):
        if username is None:
            raise AttributeError("Username пользователя должен быть представлен")
        if email is None:
            raise AttributeError("Email пользователя должен быть представлен")
        if password is None:
            raise AttributeError("Пароль пользователя должен быть представлен")
        validate_password(password)


class User(AbstractUser):

    class Meta:
        db_table = 'user'
        unique_together = ('username','email')
