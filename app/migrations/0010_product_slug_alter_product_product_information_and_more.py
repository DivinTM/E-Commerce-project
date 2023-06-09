# Generated by Django 4.1.1 on 2023-02-28 11:29

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_product_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_information',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterModelTable(
            name='product',
            table='app_Product',
        ),
    ]
