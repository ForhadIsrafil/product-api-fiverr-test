from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase, APIRequestFactory, APIClient, RequestsClient
from product.models import Product, Variant
import json
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.test import force_authenticate


class ProductTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('product.urls')),
        path('api/', include('user.urls')),
    ]
    def setUp(self):
        user, is_true = User.objects.get_or_create(username="ifeee007")
        user.check_password("lasdfkj")
        if user.is_authenticated:
            token, created = Token.objects.get_or_create(user=user)
            self.token = token.key
            print('Token ',self.token)

    def test_user_signup(self):
        url = reverse('user:signup')
        data = {
            "first_name": "forhad",
            "last_name": "israfil",
            "username": "ifi007",
            "email": "ifi@gmail.com",
            "password": "lasdfkj"
        }
        response = self.client.post(url, data, 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        print('signup..........done')

    def test_create_product(self):
        url = reverse('product:create_product')
        data = {
            'name': 'product 23',
            '_class': 'Dry Food',
            'price': 220,
            'status': 'available',
            'image': "https://images.unsplash.com/photo-1598799170815-933217492614",
            'variant': ['de74699d12494dda82f0e14f3e219cb6','7308afe2-fbfd-46b6-9aac-4094a83be4ee', ]
        }

        response = self.client.post(path=url, data=data, HTTP_AUTHORIZATION="Token " + self.token,)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 1)
