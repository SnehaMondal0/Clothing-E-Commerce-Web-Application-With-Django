from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Size, Color, Product, Cart, CartItem, Order, OrderItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class CategorySerializer(serializers.ModelSerializer):
    section_display = serializers.CharField(source='get_section_display', read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'section', 'section_display', 'name', 'slug', 'image']

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name', 'code']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    sizes = SizeSerializer(many=True, read_only=True)
    colors = ColorSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price', 'discount_price', 'description', 'image', 'sizes', 'colors', 'stock', 'created_at']

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'size', 'color', 'quantity', 'total_price']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'session_id', 'created_at', 'items']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'size', 'color', 'quantity', 'price', 'line_total']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'full_name', 'address', 'city', 'phone', 'subtotal', 'discount', 'total_amount', 'payment_status', 'status', 'ordered_at', 'updated_at', 'items']
