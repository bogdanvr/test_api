from django.db import models

import users.models
from django.db import models


class Message(models.Model):
    """"""
    created = models.DateTimeField('Сообщение создано', auto_now_add=True)
    text = models.TextField('Текст сообщения')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE,
                             verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self) -> str:
        created = f'{self.created:%d.%m.%Y, %H:%M}'
        return f'{self.user} написал сообщение {created}'
