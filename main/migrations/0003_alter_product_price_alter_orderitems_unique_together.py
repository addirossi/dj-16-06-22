# Generated by Django 4.0.5 on 2022-06-16 17:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_order_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterUniqueTogether(
            name='orderitems',
            unique_together={('order', 'product')},
        ),
    ]
