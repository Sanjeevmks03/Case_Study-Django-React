# Generated by Django 3.2.12 on 2023-04-30 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0004_alter_profilemodel_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
