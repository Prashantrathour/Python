# Generated by Django 4.2.4 on 2023-08-10 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_menu', '0002_alter_dish_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='dish_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]