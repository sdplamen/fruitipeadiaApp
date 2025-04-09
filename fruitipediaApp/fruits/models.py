from django.core.validators import MinLengthValidator
from django.db import models

from .validators import name_validator


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

class Fruit(models.Model):
    name = models.CharField(max_length=30, unique=True, validators=[MinLengthValidator(2), name_validator])
    image_url = models.URLField()
    description = models.TextField()
    nutrition = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='fruits')