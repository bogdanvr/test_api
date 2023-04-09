from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from tax.filters import TaxFilter
from words.filters import PhraseFilter
from words.models import Words, Phrases
from tax.serializers.tax_serializer import TaxSerializer
from words.serializers.phrase_serializer import PhraseSerializer
from words.serializers.word_serializer import WordSerializer
from rest_framework.response import Response


class WordModelViewSet(ModelViewSet):
    queryset = Words.objects.all()
    serializer_class = WordSerializer
    filter_backends = DjangoFilterBackend,

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        print(f'views args - {args} kwargs {kwargs}')
        print('request', request.data)
        response = super().create(request, *args, **kwargs)
        instance = response.data
        print('instance', instance)
        return Response({'status': 'success'})

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class PhraseModelViewSet(ModelViewSet):
    queryset = Phrases.objects.select_related('word')
    serializer_class = PhraseSerializer
    filter_backends = DjangoFilterBackend,
    filterset_class = PhraseFilter

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        print(f'views args - {args} kwargs {kwargs}')
        print('request', request.data)
        response = super().create(request, *args, **kwargs)
        instance = response.data
        print('instance', instance)
        return Response({'status': 'success'})

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
