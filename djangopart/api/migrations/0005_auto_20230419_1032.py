# Generated by Django 3.2.12 on 2023-04-19 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='email',
            field=models.EmailField(default='SOME STRING', max_length=254),
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(default='SOME STRING', max_length=254),
        ),
    ]