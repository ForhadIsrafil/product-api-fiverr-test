from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *
from rest_framework.authtoken.models import Token


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    variant = VariantSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', '_class', 'price', 'image', 'status', 'variant',)
        # extra_kwargs = {'variant': {'write_only': True}}

    def validate(self, attrs):
        data = super(ProductSerializer, self).validate(attrs)
        return data


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', '_class', 'price', 'image', 'status', 'variant',)

    # def validate(self, attrs):
    #     data = super(CreateProductSerializer, self).validate(attrs)
    #     return data
