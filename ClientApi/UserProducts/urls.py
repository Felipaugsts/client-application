from django.urls import path
from .views import get_products, edit_product, create_post, delete_product

urlpatterns = [
     path('post', create_post, name='create_post'),  
     path('products', get_products, name="get_products"),
     path('products/<uuid:productID>', edit_product, name='edit_product'),
     path('product/<uuid:productID>', delete_product, name='delete_product'),
]
