from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from tax.filters import TaxFilter
from tax.models import Tax
from tax.serializers.tax_serializer import TaxSerializer


class TaxModelViewSet(ModelViewSet):
    """ Вьюсет заявок. """

    queryset = Tax.objects.all()
    serializer_class = TaxSerializer
    filter_backends = DjangoFilterBackend,
    filterset_class = TaxFilter

    def list(self, request, *args, **kwargs):
        """ Список заказов. """
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """ Детальная информация о заказе. """
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """ Создать заказ. """
        print(f'views args - {args} kwargs {kwargs}')
        print('request', request.data)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """ Изменить заказ. """
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """ Частитчно изменить заказ. """
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """ Удалить заказ. """
        return super().destroy(request, *args, **kwargs)
