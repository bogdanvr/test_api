import django_filters
from rest_framework import filters

from tax.models import Tax


class TaxFilter(django_filters.rest_framework.FilterSet):
    chat_id = django_filters.NumberFilter(field_name='user__chat_id')

    class Meta:
        model = Tax
        fields = ('user', 'chat_id')
