# Generated by Django 3.2.12 on 2023-04-26 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_cart_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.IntegerField(default=0),
        ),
    ]