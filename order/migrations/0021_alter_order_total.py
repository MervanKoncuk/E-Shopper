# Generated by Django 4.0.6 on 2022-12-09 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0020_order_is_it_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.IntegerField(),
        ),
    ]
