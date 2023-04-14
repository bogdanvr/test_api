import django_filters

from words.models import Phrases, Words


class WordsFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Words
        fields = ('word',)


class PhraseFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Phrases
        fields = ('word',)
