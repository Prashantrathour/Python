# Generated by Django 4.2.4 on 2023-08-10 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=5),
        ),
    ]
