from rest_framework import serializers
from .models import Product, Category, Firm, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'description', 'price', 'available', 'created')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = ('id', 'name')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'country', 'first_name', 'last_name', 'company_name', 'email', 'phone', 'address', 'postal_code', 'order_notes', 'created', 'updated', 'paid')

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'price', 'quantity')