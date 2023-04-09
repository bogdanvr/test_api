from rest_framework import serializers

from words.models import Words
from words.serializers.phrase_serializer import PhraseSerializer


class WordSerializer(serializers.ModelSerializer):
    word = serializers.CharField()
    translate = serializers.CharField()

    class Meta:
        model = Words
        fields = ('id', 'word', 'translate', 'user')

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
