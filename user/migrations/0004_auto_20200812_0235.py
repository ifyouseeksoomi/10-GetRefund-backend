# Generated by Django 3.0.8 on 2020-08-12 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200808_0906'),
        ('order', '0002_auto_20200811_1549'),
        ('user', '0003_user_order_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='order_item',
        ),
        migrations.AddField(
            model_name='user',
            name='items',
            field=models.ManyToManyField(related_name='order_item', through='order.Order', to='product.Product'),
        ),
    ]
