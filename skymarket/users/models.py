from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from users.managers import UserManager

NULLABLE = {'null': True, 'blank': True}


class User(AbstractBaseUser, PermissionsMixin):
    """
      Модель пользователя.

       Атрибуты класса:
        USERNAME_FIELD (str): Имя поля, используемого в качестве уникального идентификатора пользователя.
        REQUIRED_FIELDS (list): Список полей, требуемых при создании пользователя.

    Методы:
        __str__(): Возвращает строковое представление пользователя.

    Метаданные:
        verbose_name (str): Человекочитаемое имя модели.
        verbose_name_plural (str): Человекочитаемое множественное имя модели.
    """
    ROLE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]

    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    phone = PhoneNumberField(unique=False, verbose_name='Телефон', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Email')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, verbose_name='Роль', **NULLABLE)
    image = models.ImageField(upload_to='avatars/', **NULLABLE, verbose_name='Изображение')

    is_staff = models.BooleanField(default=False, verbose_name='Является сотрудником')
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
