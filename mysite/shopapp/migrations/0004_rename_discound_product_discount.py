# Generated by Django 4.2.5 on 2023-09-16 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0003_product_archived'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discound',
            new_name='discount',
        ),
    ]
