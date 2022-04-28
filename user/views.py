from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import filters, status
from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from .utils import get_object
import json
from .models import *
from .serializers import *

# todo: creating new user
class CreateUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data={"success": True}, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# todo: View for user login
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        data = request.data
        user = authenticate(request, username=data['username'].strip(), password=data['password'].strip())
        if user:
            serializer = LoginSerializer(user, data=request.data, context={"request": request})
            if serializer.is_valid():
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={"error": "User not found!"}, status=status.HTTP_404_NOT_FOUND)
