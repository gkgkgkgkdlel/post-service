from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
