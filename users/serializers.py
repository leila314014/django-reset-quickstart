from rest_framework import serializers

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from .models import User


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_superuser',
            'is_staff',
            'is_active',
            'name',
            'image',
        ]

    def get_name(self, user):
        return f'{user.first_name} {user.last_name }'.strip()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class PasswordSetSerializer(serializers.Serializer):
    password = serializers.CharField()
    password_confirm = serializers.CharField()

    def validate(self, attrs):
        user = self.context['request'].user

        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({
                'password': 'Password not match.',
                'password_confirm': 'Password not match.',
            })

        try:
            validate_password(attrs['password'], user)
        except ValidationError as e:
            raise serializers.ValidationError({
                'password': e.messages,
            })

        return attrs


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
