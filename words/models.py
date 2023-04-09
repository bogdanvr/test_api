from django.db import models


class Words(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    word = models.CharField(max_length=150, verbose_name='Слово')
    translate = models.CharField(max_length=150, verbose_name='Перевод')

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'

    def __str__(self) -> str:
        return self.word


class Phrases(models.Model):
    word = models.ForeignKey(Words, related_name='relatedword', on_delete=models.CASCADE)
    phrase = models.CharField(max_length=300, verbose_name='Фраза')
    translate = models.CharField(max_length=300, verbose_name='Перевод фразы')

    class Meta:
        verbose_name = 'Фраза'
        verbose_name_plural = 'Фразы'

    def __str__(self) -> str:
        return self.phrase
