# Generated by Django 4.2.4 on 2023-08-10 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_menu', '0003_dish_dish_name_alter_dish_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cutomer_name', models.CharField(max_length=100)),
                ('quatity', models.IntegerField()),
                ('status', models.CharField(choices=[('received', 'Received'), ('preparing', 'Preparing'), ('ready', 'Ready for Pickup'), ('delivered', 'Delivered')], default='received', max_length=20)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('dish_name', models.ManyToManyField(to='item_menu.dish')),
            ],
        ),
    ]
