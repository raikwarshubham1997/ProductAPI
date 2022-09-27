from dataclasses import field
from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"
        # fields =  ['id', 'title', 'availableStock']

class ProductSerializer(serializers.ModelSerializer):
    # variants = serializers.CharField(source='variants.title')
    variants = CategorySerializer(read_only=True,many=True)
    print(variants)
    class Meta:
        model = Product
        # fields = "__all__"
        fields =  ['id', 'name', 'Class', 'variants', 'price', 'image', 'stock', 'status']

