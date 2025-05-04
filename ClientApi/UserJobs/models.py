from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=255)
    seniority = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    technology = models.CharField(max_length=255)
    link = models.URLField()
    description = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=255)
    remote = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')


