# Generated by Django 3.2.4 on 2021-06-28 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetail',
            name='product',
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='product',
            field=models.ManyToManyField(to='product.Product'),
        ),
    ]