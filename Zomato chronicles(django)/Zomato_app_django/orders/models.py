from django.db import models
from item_menu.models import Dish

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    dish_ids = models.ManyToManyField(Dish, related_name='orders')
 
    status_choices = [
        ('received', 'Received'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready for Pickup'),
        ('delivered', 'Delivered'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='received')
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f"Order #{self.pk}: {self.customer_name}"
