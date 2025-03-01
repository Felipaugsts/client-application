from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import PostSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from django.views.decorators.csrf import csrf_exempt

@api_view(['POST'])
def create_post(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        data = request.data.copy()
        data['user'] = request.user.id 

        serializer = PostSerializer(data=data, context={'request': request})

        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
 
@api_view(['GET'])
@permission_classes([AllowAny])
def get_products(request): 
    if request.method == 'GET':
        product = Product.objects.all()

        serializer = PostSerializer(product, many=True)
        return Response(serializer.data)
    
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT'])
def edit_product(request, productID):
    if request.method == 'PUT':
        try:
            print('productID', productID)
            product = Product.objects.get(productID=productID)
        except Product.DoesNotExist:
            return Response({'detail': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)

        if product.user != request.user:
            return Response({'detail': 'You do not have permission to edit this product.'}, status=status.HTTP_403_FORBIDDEN)
        
        product.title = request.data.get('title', product.title)
        product.description = request.data.get('description', product.description)
        product.imageUrl = request.data.get('imageUrl', product.imageUrl)

        product.save()

        return Response({'detail': 'Product updated successfully.'}, status=status.HTTP_200_OK)
    
@csrf_exempt  
@api_view(['DELETE'])
def delete_product(request, productID):
    if request.method == 'DELETE': 
        try: 
            product = Product.objects.get(productID=productID)
        except Product.DoesNotExist:
            return Response({'detail': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        if product.user != request.user:
            return Response({'detail': 'You do not have permission to edit this product.'}, status=status.HTTP_403_FORBIDDEN)
        
        product.delete()

        return Response({'detail': 'Product was successfully deleted.'}, status=status.HTTP_200_OK)