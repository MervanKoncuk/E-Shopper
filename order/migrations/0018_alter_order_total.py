# Generated by Django 4.0.6 on 2022-12-09 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0017_alter_order_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
