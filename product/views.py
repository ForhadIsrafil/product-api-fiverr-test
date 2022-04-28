from django.db.models import Q
from .utils import get_object
from rest_framework import status
from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import *


# todo: View for create new products
class CreateProductView(viewsets.GenericViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer

    # todo: createing new products
    def create(self, request, format=None):
        print(request.data)
        serializer = CreateProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"success": True}, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# todo: view for UPDATE, DELETE, GET a single product
class ProductView(viewsets.GenericViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # todo: UPDATE an existing product
    def update(self, request, id, format=None):
        product_ins = get_object(Product, id)
        if product_ins is not None:
            serializer = ProductSerializer(product_ins, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(data={"success": True}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={"Error": "Data Not Found!"}, status=status.HTTP_404_NOT_FOUND)

    # todo: DELETE an existing product
    def destroy(self, request, id, format=None):
        product_ins = get_object(Product, id)
        if product_ins is not None:
            product_ins.delete()
            return Response(data={"success": True}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data={"Error": "Data Not Found!"}, status=status.HTTP_404_NOT_FOUND)

    # todo: GET an existing product
    def retrive(self, request, id, format=None):
        product_ins = get_object(Product, id)
        if product_ins is not None:
            serializer = ProductSerializer(product_ins)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={"Error": "Data Not Found!"}, status=status.HTTP_404_NOT_FOUND)

# todo: SEARCH products by product [name, class, status]
class SearchProducts(viewsets.GenericViewSet, mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # todo: get list of products by searching with name or class or status
    def list(self, request, *args, **kwargs):
        if request.GET.get('search'):
            query = request.GET.get('search')
            product_ins = Product.objects.filter(
                Q(name__contains=request.GET.get('search')) | Q(_class=request.GET.get('search')) | Q(
                    status=request.GET.get('search')))
            serializer = ProductSerializer(product_ins, many=True)
            return Response(data={"data": serializer.data}, status=status.HTTP_200_OK)
        return Response(data={"data": ProductSerializer(self.queryset, many=True).data}, status=status.HTTP_200_OK)

