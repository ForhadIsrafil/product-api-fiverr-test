from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator


class Variant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    availableStock = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS_CHOICES = (
        ("available", "Available"),
        ("unavailable", "Unavailable")
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    _class = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.URLField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="available")  # unavailable
    variant = models.ManyToManyField(Variant)

    def __str__(self):
        return f"Name: {self.name} Class: {self._class}"
