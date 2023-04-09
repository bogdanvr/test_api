from rest_framework import serializers

from words.models import Phrases, Words


class PhraseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phrases
        fields = ('id', 'phrase', 'translate', 'word')

    def create(self, validated_data):
        print('validated_data', validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
