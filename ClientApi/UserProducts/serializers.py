from rest_framework import serializers
from .models import Product

from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['productID', 'user', 'title', 'description', 'imageUrl', 'created_at', 'isNew', 'price', 'rate' ]

    def create(self, validated_data):
        # Criação do produto com o usuário
        return Product.objects.create(**validated_data)
