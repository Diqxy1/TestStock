# Generated by Django 3.0.8 on 2020-07-21 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200721_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.DecimalField(decimal_places=0, max_digits=5, verbose_name='Quantidade'),
        ),
    ]
