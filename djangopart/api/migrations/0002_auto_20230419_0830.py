# Generated by Django 3.2.12 on 2023-04-19 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addproduct',
            name='category',
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Signup',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.DeleteModel(
            name='UpdateProfile',
        ),
        migrations.DeleteModel(
            name='AddProduct',
        ),
        migrations.DeleteModel(
            name='category',
        ),
        migrations.DeleteModel(
            name='subcategory',
        ),
    ]
