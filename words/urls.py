from django.urls import path, include
from rest_framework.routers import DefaultRouter

from words.views import WordModelViewSet, PhraseModelViewSet

router = DefaultRouter()
router.register(r'word', WordModelViewSet, basename="word")
router.register(r'phrase', PhraseModelViewSet, basename="word")

urlpatterns = [
    path('', include(router.urls)),
]
