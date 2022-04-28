from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *
from rest_framework.authtoken.models import Token


# todo: serializer for creating new users
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        data = validated_data
        instance = User.objects.create_user(first_name=data['first_name'], last_name=data['last_name'], username=data['username'],
                        email=data['email'], )
        instance.set_password(raw_password=data['password'])
        instance.is_active = True
        instance.save()
        return instance

# todo: User Login serializer for Token
class LoginSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'token')

    def get_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj)
        return token.key



