from django.urls import path

from users.views import CreateUserView, CustomObtainAuthToken

urlpatterns = [
    path('api-token-auth/', CustomObtainAuthToken.as_view(), name='api-token-auth'),
    path('create-user/', CreateUserView.as_view()),
]
