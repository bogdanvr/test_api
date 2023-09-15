from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from pages.models import Ads
from pages.serializers.ads_serializer import AdsSerializer


class ListCreateAds(ListCreateAPIView):
    """Получение списка и создание сообщения"""
    permission_classes = IsAuthenticated,
    model = Ads
    serializer_class = AdsSerializer
    # filter_backends = UserFilterChat,
    queryset = Ads.objects.all()

    def post(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)