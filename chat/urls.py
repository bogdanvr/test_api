from django.urls import path

from chat.views import ListCreateMessages, GenerateTelegramToken, CheckTelegramToken

urlpatterns = [
    path('', ListCreateMessages.as_view()),
    path('generate_telegram_token/', GenerateTelegramToken.as_view()),
    path('check_telegram_token/', CheckTelegramToken.as_view()),
]
