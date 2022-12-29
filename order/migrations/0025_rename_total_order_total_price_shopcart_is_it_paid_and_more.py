# Generated by Django 4.0.6 on 2022-12-09 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0024_remove_order_product_order_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total',
            new_name='total_price',
        ),
        migrations.AddField(
            model_name='shopcart',
            name='is_it_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shopcart',
            name='total',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
