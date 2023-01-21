from rest_framework import status
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.settings import api_settings

from chat.filters import UserFilterChat
from chat.models import Message
from chat.serializers.chat_serializer import ChatSerializer
from chat.serializers.telegram_token_serializer import TelegramTokenSerializer, CheckTelegramTokenSerializer
from chat.services import check_telegram_token, send_message_to_telegram
from users.models import User


class ListCreateMessages(ListCreateAPIView):
    """Получение списка и создание сообщения"""
    permission_classes = IsAuthenticated,
    model = Message
    serializer_class = ChatSerializer
    filter_backends = UserFilterChat,
    queryset = Message.objects.all()

    def post(self, request, *args, **kwargs):
        """Отправка сообщения в телеграмм"""
        send_message_to_telegram(
            chat_id=request.user.chat_id,
            user=request.user,
            text=request.data['text']
        )
        return self.create(request, *args, **kwargs)


class GenerateTelegramToken(CreateAPIView):
    """Генерирует телеграмм токен"""
    permission_classes = IsAuthenticated,
    model = User
    serializer_class = TelegramTokenSerializer


class CheckTelegramToken(APIView):
    """Проверяет полученный токен от телеграмм"""
    permission_classes = AllowAny,

    def post(self, request):
        serializer = CheckTelegramTokenSerializer(data=request.data)
        if serializer.is_valid():
            data = request.data
            result = check_telegram_token(data.get('telegram_token'), data.get('chat_id'))
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
