from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=255,unique=True)
    description = models.TextField(null=True, blank=True)

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quitantity = models.PositiveBigIntegerField(default=0)
    image = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')