# Generated by Django 4.0.6 on 2022-11-24 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0028_alter_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
