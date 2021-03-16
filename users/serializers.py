from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import Client, User
from .services import send_auth_token_to_email


class UserCreateSerializer(serializers.ModelSerializer):
    """Список пользователей"""
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)

    def validate_password(self, value):
        try:
            validate_password(value)
        except serializers.ValidationError as exc:
            raise serializers.ValidationError(str(exc))
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            is_active=False,
        )
        send_auth_token_to_email(user_obj=user)

        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserListSerializer(serializers.ModelSerializer):
    """Список пользователей"""

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active')


class ClientListSerializer(serializers.ModelSerializer):
    """Список клиентов"""
    user = UserListSerializer()

    class Meta:
        model = Client
        fields = '__all__'
