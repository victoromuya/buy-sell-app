# Generated by Django 4.0 on 2022-07-16 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=1.2),
            preserve_default=False,
        ),
    ]
