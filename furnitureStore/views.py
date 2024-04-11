from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product, Category, Firm, Order, OrderItem
from .serializers import ProductSerializer, CategorySerializer, FirmSerializer, OrderSerializer, OrderItemSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ('get', 'post', 'put', 'delete')
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    @action(detail = False, methods = ['GET'])
    def available(self, request):
        available_products = self.get_queryset().filter(available = True)
        serializer = self.get_serializer_class()(available_products, many=True)
        return Response(data=serializer.data)

    @action(detail = True, methods= ['POST'])
    def make_available(self, request, pk):
        product = self.get_object()
        product.available = True
        product.save()

        return Response({"message": f"Товар '{product.name}' помечен как 'в наличии'."}, status=228)

    @action(detail=True, methods=['POST'])
    def make_unavailable(self, request, pk):
        product = self.get_object()
        product.available = False
        product.save()

        return Response({"message": f"Товар '{product.name}' помечен как 'не в наличии'."}, status=228)






class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ('get', 'post', 'put', 'delete')
    permission_classes = [IsAdminUser]


class FirmViewSet(ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    http_method_names = ('get', 'post', 'put', 'delete')
    permission_classes = [IsAdminUser]


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ('get', 'post', 'put', 'delete')
    permission_classes = [IsAuthenticated]



class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    http_method_names = ('get', 'post', 'put', 'delete')
    permission_classes = [IsAuthenticated]




