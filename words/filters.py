import django_filters

from words.models import Phrases


class PhraseFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Phrases
        fields = ('word',)
