from django.urls import path
from . import views

urlpatterns = [
    path('create-product', views.CreateProductView.as_view({'post': 'create'})),
    path('product/<str:id>', views.ProductView.as_view({'patch': 'update', 'delete': 'destroy', 'get': 'retrive'})),
    path('search-product', views.SearchProducts.as_view({'get': 'list'})),
]
