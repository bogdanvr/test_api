from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models

class User(AbstractUser):
    """ Пользователь. """

    name = models.CharField('имя', max_length=150)
    telegram_token = models.CharField('Телеграм токен', max_length=32, blank=True, null=True)
    chat_id = models.CharField('chat_id', max_length=32, blank=True, null=True)

    default = UserManager()

    def __str__(self) -> str:
        return self.username