from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING
from product.models import Product
# Create your models here.

class Order(models.Model):
    order_customer = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'order'
        verbose_name_plural = 'orders'


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, default='', on_delete=models.CASCADE)
    product = models.OneToOneField(Product, blank=False, on_delete=DO_NOTHING)
    quantity = models.IntegerField(blank=False)