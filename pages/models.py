from django.db import models


class Ads(models.Model):
    page_id = models.PositiveIntegerField(unique=True, verbose_name='Идентификатор')
    title = models.CharField(max_length=300, verbose_name='Название')
    url = models.URLField( verbose_name='Ссылка на детальную страницу')
    views = models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество просмотров')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self) -> str:
        return self.title
