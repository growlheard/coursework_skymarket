from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
# TODO Здесь нам придется переопределить сериалайзер, который использует djoser
# TODO для создания пользователя из за того, что у нас имеются нестандартные поля


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    """
        Сериализатор для регистрации пользователя.
    """
    phone = PhoneNumberField(required=True, write_only=True,)

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'phone', 'image')


class CurrentUserSerializer(serializers.ModelSerializer):
    """
        Сериализатор для текущего пользователя.
    """
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'phone', 'role', 'image')

