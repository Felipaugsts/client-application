from django.db import models
from django.contrib.auth.models import User
import uuid

class Product(models.Model):
    productID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    imageUrl = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    isNew = models.BooleanField(auto_created=True, default=False)
    price = models.IntegerField(default=0)
    rate = models.IntegerField()

    def __str__(self):
        return self.title
