from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from users.models import User


class UserAdminSerializer(BaseUserRegistrationSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}