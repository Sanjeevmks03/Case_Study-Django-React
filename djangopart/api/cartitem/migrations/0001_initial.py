# Generated by Django 3.2.12 on 2023-04-25 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Product', '0004_alter_products_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.products')),
            ],
        ),
    ]
