from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиент'


class EmailAuthToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.UUIDField()

    def __str__(self):
        return f'Токен для {self.user.username}'

    class Meta:
        verbose_name = 'Токен для Активации Пользователя'
        verbose_name_plural = 'Токены для Активации Пользователей'
