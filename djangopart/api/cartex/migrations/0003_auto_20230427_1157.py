# Generated by Django 3.2.12 on 2023-04-27 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartex', '0002_alter_cartex_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartex',
            name='productid',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='cartex',
            name='userid',
            field=models.IntegerField(default=0),
        ),
    ]
