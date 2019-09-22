from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager


class Word(models.Model):
    name = models.CharField('Слово', max_length=30)
    translation = models.CharField('Перевод', max_length=64)


class User(AbstractBaseUser, PermissionsMixin):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский')
    )

    email = models.CharField('Электронная почта', max_length=64, unique=True, null=True, default=None, blank=True)
    password = models.CharField(max_length=64)
    salt = models.CharField(max_length=64)
    nickname = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField('Пол', max_length=1, choices=GENDER_CHOICES, default=MALE)
    birth_date = models.DateField('Дата рождения', null=True, blank=True)
    learning_words = models.ManyToManyField(Word, related_name='learning_users')
    learned_words = models.ManyToManyField(Word, related_name='learned_users')
    is_superuser = models.BooleanField(default=False)
    cookie = models.CharField(max_length=64, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'nickname'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        default_permissions = ()