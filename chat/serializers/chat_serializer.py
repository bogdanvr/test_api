from rest_framework import serializers

from chat.models import Message
from users.models import User


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('created', 'text')
        read_only_fields = ('user',)

    def create(self, validated_data):
        user = self.context.get("request").user
        message = Message.objects.create(
            text=validated_data['text'],
            user=user
        )
        message.save()
        return message
