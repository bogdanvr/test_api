from rest_framework import serializers

from tax.models import Tax


class TaxSerializer(serializers.ModelSerializer):
    start = serializers.DateTimeField(default='')
    arrived = serializers.DateTimeField(default='')
    process = serializers.DateTimeField(default='')
    completed = serializers.DateTimeField(default='')
    price = serializers.IntegerField()
    payment_type = serializers.IntegerField(default=None)
    status = serializers.IntegerField()

    class Meta:
        model = Tax
        fields = ('user', 'start', 'arrived', 'process', 'completed', 'price',
                  'payment_type', 'status')

    def create(self, validated_data):
        return Tax(**validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
