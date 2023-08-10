from django.shortcuts import render, redirect
from .forms import OrderForm
from orders.models import Order  # Make sure to import the Dish model
from .models import Dish

def all_dishes(request):
    dishes = Dish.objects.all()
    return render(request, 'take_order.html', {'dishes': dishes})
def take_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')  # Redirect to the order list page
    else:
        form = OrderForm()
    return render(request, 'take_order.html', {'form': form})
def orders(request):
    orders = Order.objects.all()
    print(orders)
    return render(request, 'order_list.html',{orders:orders})