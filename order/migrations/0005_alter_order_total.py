# Generated by Django 4.0.6 on 2022-11-27 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_adminnote_alter_order_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.FloatField(null=True),
        ),
    ]
