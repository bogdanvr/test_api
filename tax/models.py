from django.db import models
from django.db.models import IntegerChoices


class Statuses(IntegerChoices):
    OPENED = 1, 'Принят'
    CLOSED = 3, 'Выполнен'
    CANCELED = 4, 'Отменён'


class PaymentType(IntegerChoices):
    CASH = 1, 'Наличные'
    CARD = 2, 'Карта'
    KASPI = 3, 'Каспи'


class Tax(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    start = models.DateTimeField(blank=True, null=True, verbose_name='Старт')
    arrived = models.DateTimeField(blank=True, null=True, verbose_name='Прибыл')
    process = models.DateTimeField(blank=True, null=True, verbose_name='В процессе')
    completed = models.DateTimeField(blank=True, null=True, verbose_name='Завершил')
    price = models.IntegerField(verbose_name='Стоимость', blank=True, default=0)
    payment_type = models.PositiveSmallIntegerField(choices=PaymentType.choices, blank=True, null=True,
                                    verbose_name='Тип оплаты')
    status = models.PositiveSmallIntegerField(choices=Statuses.choices, default=Statuses.OPENED,
                              verbose_name='Статус заявки')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self) -> str:
        created = f'{self.created:%d.%m.%Y, %H:%M}'
        return f'Заявка №{self.id} от {created}'
