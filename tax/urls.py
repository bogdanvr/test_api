from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tax.views import TaxModelViewSet

router = DefaultRouter()
router.register(r'order', TaxModelViewSet, basename="tax")

urlpatterns = [
    path('', include(router.urls)),
]
