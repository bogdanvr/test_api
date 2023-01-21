import uuid

from rest_framework import serializers

from chat.services import generate_token_for_telegram
from users.models import User


class TelegramTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('telegram_token',)

    def create(self, validated_data):
        user = User.objects.get(id=self.context.get('request').user.id)
        telegram_token = generate_token_for_telegram()
        user.telegram_token = telegram_token
        user.save()
        return user

class CheckTelegramTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('telegram_token',)

    def validate(self, data):
        if data.get('telegram_token'):
            print('data', data)
            try:
                uuid.UUID(str(data.get('telegram_token')))
            except ValueError:
                raise serializers.ValidationError("you sent do not valid UUID")
            return data
        else:
            raise serializers.ValidationError("you don't sent telegram_token")



