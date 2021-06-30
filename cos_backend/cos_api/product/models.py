from django.db import models

MAX_PRICE = 1000000
MIN_PRICE = 0
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100, blank=False)
    unit_price = models.IntegerField(blank=False)

    class Meta:
        db_table = 'product'
        verbose_name_plural = 'products'