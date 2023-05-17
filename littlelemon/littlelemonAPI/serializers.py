from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.CharField(read_only=True)
    class Meta:
        model = models.Category
        fields = ['id', 'slug', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = models.MenuItem
        fields = ['id', 'title', 'price', 'featured', 'category', 'category_id']

class CartSerializer(serializers.ModelSerializer):
    unit_price = serializers.DecimalField(read_only=True, max_digits=6, decimal_places=2)
    price = serializers.DecimalField(read_only=True, max_digits=6, decimal_places=2)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = models.Cart
        fields = ['user', 'menuitem', 'quantity', 'unit_price', 'price']    

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = ['id', 'order', 'menuitem', 'quantity', 'unit_price', 'price']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = models.Order
        fields = ['id', 'user', 'delivery_crew', 'status', 'order_items', 'total', 'date']

class OrderDetailSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(read_only = True, many = True)
    class Meta:
        model = models.Order
        fields = ['order_items']
