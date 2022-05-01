from django.urls import path
from . import views
app_name = 'product'
urlpatterns = [
    path('create-product', views.CreateProductView.as_view({'post': 'create'}), name='create_product'),
    path('product/<uuid:id>', views.ProductView.as_view({'patch': 'update', 'delete': 'destroy', 'get': 'retrive'}),
         name='single_product'),
    path('search-product', views.SearchProducts.as_view({'get': 'list'}), name='search_product'),
]
