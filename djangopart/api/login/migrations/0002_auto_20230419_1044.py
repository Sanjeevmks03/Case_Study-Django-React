# Generated by Django 3.2.12 on 2023-04-19 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='email',
        ),
        migrations.AddField(
            model_name='login',
            name='password',
            field=models.CharField(default='some string', max_length=50),
        ),
    ]