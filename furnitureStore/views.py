from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product, Category, Firm, Order, OrderItem
from .serializers import ProductSerializer, CategorySerializer, FirmSerializer, OrderSerializer, OrderItemSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ('get', 'post', 'put', 'delete')


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ('get', 'post', 'put', 'delete')


class FirmViewSet(ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    http_method_names = ('get', 'post', 'put', 'delete')


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ('get', 'post', 'put', 'delete')


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    http_method_names = ('get', 'post', 'put', 'delete')

