# # from django.shortcuts import render, get_object_or_404, redirect

# from django.shortcuts import render, redirect,get_object_or_404
# from .models import Dish, Order, OrderQuantity
# def add_dish(request):
#     if request.method == 'POST':
#         dish_name = request.POST['dish_name']
#         price = request.POST['price']
#         availability = request.POST.get('availability', False)
#         # Dish.objects.create( price=12.99, availability=True)
#         availability=True if availability=="on"  else False
     
#         Dish.objects.create(dish_name=dish_name, price=float(price), availability=availability)
#         return redirect('dish_list')

#     return render(request, 'add_dish.html')

# def dish_list(request):
#     dishes = Dish.objects.all()
#     return render(request, 'dish_list.html', {'dishes': dishes})
# def remove_dish(request, dish_id):
#     dish = Dish.objects.get(id=dish_id)
#     dish.delete()
#     return redirect('dish_list')
# def remove_order(request, dish_id):
#     order = Order.objects.get(id=dish_id)
#     order.delete()
#     return redirect('display_order')
# def update(request, dish_id):
#     dish = Dish.objects.get(id=dish_id)
    
#     if request.method == 'POST':
#         dish.dish_name = request.POST.get('dish_name')
#         dish.price = float(request.POST.get('price'))
#         dish.availability =True if request.POST.get('availability') == 'on' else False
#         print(request.POST.get('availability'))
#         dish.save()
      
#         return redirect('dish_list')
    
#     return render(request, 'edit.html', {'dish': dish})



# def update_order(request, order_id):
#     order = get_object_or_404(Order, pk=order_id)
    
#     if request.method == 'POST':
#         # Update the order status or other details here
#         order.status = request.POST.get('status')
#         print( "change",request.POST.get('status'))
#         order.save()
#         return redirect('display_orders')
    
#     return render(request, 'update_order.html', {'order': order})

# def cancel_order(request, order_id):
#     order = get_object_or_404(Order, pk=order_id)
#     # get_object_or_404(OrderQuantity, pk=order_id).delete()
#     order.delete()
#     return redirect('display_orders')
    
#     # return render(request, 'cancel_order.html', {'order': order})

# # views.py

# def take_order(request, dish_id):
#     if request.method == 'POST':
#         cutomer_name = request.POST['cutomer_name']
#         selected_dish_ids = [int(dish_id) for dish_id in request.POST.getlist('selected_dishes[]')]
#         quantities = [int(quantity) for quantity in request.POST.getlist('dish_quantity[]')]

#         selected_dishes = Dish.objects.filter(id__in=selected_dish_ids)
        
#         if selected_dishes.exists():
#             new_order = Order(cutomer_name=cutomer_name)
#             new_order.save()

#             for dish, quantity in zip(selected_dishes, quantities):
#                 if quantity > 0:
#                     order_quantity = OrderQuantity(order=new_order, dish=dish, quantity=quantity,dish_name=dish)
#                     order_quantity.save()

#             new_order.save()

#         return redirect('display_orders')

#     menu = Dish.objects.all()
#     return render(request, 'take_order.html', {'menu': menu})



# # zomato/views.py

# def display_orders(request):
#     orders = Order.objects.all()
#     quantity = OrderQuantity.objects.all()
   
#     return render(request, 'display_orders.html', {'orders': orders})



# json-response
from django.shortcuts import render, redirect, get_object_or_404,Http404,get_list_or_404

from .models import Dish, Order, OrderQuantity, DeliveredOrder
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponseNotAllowed
from django.db.models import F, Sum
import json
@ csrf_exempt
def add_dish(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))  # Parse JSON data from request
            dish_name = data.get('dish_name', '')
            price = data.get('price', 0.0)
            availability = data.get('availability', False)
            Dish.objects.create(dish_name=dish_name, price=float(price), availability=availability)
            # Your logic to create a Dish object here
            
            return JsonResponse({"message": "Dish added successfully"})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    return JsonResponse({"message": "Invalid request method"})


def dish_list(request):
    dishes = Dish.objects.all()
    dish_list = [{"id": dish.id,"dish_name": dish.dish_name, "price": dish.price, "availability": dish.availability} for dish in dishes]
    return JsonResponse({"dishes": dish_list})
@csrf_exempt
def remove_dish(request, dish_id):
    if request.method == 'DELETE':
        try:
            dish = Dish.objects.get(id=dish_id)
            dish.delete()
            return JsonResponse({"message": "Dish removed successfully"})
        except Dish.DoesNotExist:
            return JsonResponse({"message":"not found"})
    else:
        return HttpResponseNotAllowed(["DELETE"])



# http://127.0.0.1:8000/update/11/
@csrf_exempt
def update(request, dish_id):    
    try:
        dish = Dish.objects.get(id=dish_id)

        if request.method == 'PATCH':
            try:
                data = json.loads(request.body.decode('utf-8'))
                
                # Update the dish attributes based on the JSON data
                if 'dish_name' in data:
                    dish.dish_name = data['dish_name']
                if 'price' in data:
                    dish.price = float(data['price'])
                if 'availability' in data:
                    dish.availability = data['availability'] == 'true'  # Assuming availability is a string 'true' or 'false' in JSON
                
                dish.save()

                return JsonResponse({"message": "Dish updated successfully"})
            except json.JSONDecodeError:
                return JsonResponse({"error": "Invalid JSON data"}, status=400)
        
        return JsonResponse({"error": "Invalid request method"}, status=405)
    except Dish.DoesNotExist:
        return JsonResponse({"error": "Dish not found"}, status=404)


@csrf_exempt


# def update_order(request, order_id):
#     try:
#         # Get all order quantity objects by order_id
#         order_quantities = get_list_or_404(OrderQuantity, order__id=order_id)
        
#         if request.method == 'PATCH':
#             try:
#                 # Parse JSON data from the request body
#                 data = json.loads(request.body.decode('utf-8'))
                
#                 # Update the order status (or any other fields you want to update) for each order quantity
#                 new_status = data.get('status')
#                 for order_quantity in order_quantities:
#                     order_quantity.order.status = new_status
#                     order_quantity.order.save()
                
#                 return JsonResponse({"message": "Orders updated successfully"})
#             except json.JSONDecodeError:
#                 return JsonResponse({"error": "Invalid JSON data"}, status=400)
        
#         return JsonResponse({"error": "Invalid request method"}, status=405)
#     except Http404:
#         return JsonResponse({"error": "Order not found"}, status=404)


def update_order(request, order_id):
    try:
        # Get all order quantity objects by order_id
        order_quantities = get_list_or_404(OrderQuantity, order__id=order_id)
        
        if request.method == 'PATCH':
            try:
                # Parse JSON data from the request body
                data = json.loads(request.body.decode('utf-8'))
                
                # Update the order status (or any other fields you want to update) for each order quantity
                new_status = data.get('status')
                for order_quantity in order_quantities:
                    order_quantity.order.status = new_status
                    order_quantity.order.save()
                    
                    # If the new status is 'delivered', move the order to DeliveredOrder model
                    if new_status == 'delivered':
                        delivered_order = DeliveredOrder(
                            order_id=order_quantity.order.id,
                            order_price=order_quantity.order.total_price,
                            customer_name=order_quantity.order.cutomer_name
                        )
                        delivered_order.save()
                        order_quantity.order.delete()
                
                return JsonResponse({"message": "Orders updated successfully"})
            except json.JSONDecodeError:
                return JsonResponse({"error": "Invalid JSON data"}, status=400)
        
        return JsonResponse({"error": "Invalid request method"}, status=405)
    except Http404:
        return JsonResponse({"error": "Order not found"}, status=404)


@csrf_exempt
def cancel_order(request, order_id):
    if request.method == 'DELETE':
        try:
            order = Order.objects.get(pk=order_id)
            order.delete()
            return JsonResponse({"message": "Order canceled successfully"})
        except Order.DoesNotExist:
            return JsonResponse({"message": "Order does not exist"})
    else:
        return JsonResponse({"message": "Invalid request method"})

@csrf_exempt

def take_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))  # Parse JSON data from request
            cutomer_name = data.get('cutomer_name', '')
            selected_dish_ids = data.get('selected_dishes', [])
            quantities = data.get('dish_quantity', [])

            selected_dishes = Dish.objects.filter(id__in=selected_dish_ids)

            if selected_dishes.exists():
                new_order = Order(cutomer_name=cutomer_name)
                new_order.save()

                order_items = []

                total_price = 0  # Initialize total price

                for dish_id, quantity in zip(selected_dish_ids, quantities):
                    dish = get_object_or_404(Dish, pk=dish_id)
                    if quantity > 0:
                        price = dish.price  # Get the price from the Dish model
                        order_quantity = OrderQuantity(order=new_order, dish=dish, quantity=quantity, dish_name=dish.dish_name)
                        order_quantity.save()
                        order_items.append({"dish_name": dish.dish_name, "quantity": quantity, "price": price})
                        total_price += price * quantity  # Update total price

                # Update the total price of the order
                new_order.total_price = total_price
                new_order.save()

                return JsonResponse({"message": "Order placed successfully", "order_id": new_order.id, "order_items": order_items, "total_price": total_price})
            else:
                return JsonResponse({"error": "Selected dishes not found"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    return JsonResponse({"message": "Invalid request method"})


def display_orders(request):
    orders = Order.objects.all()
    order_list = []

    for order in orders:
        # Get the order quantities for this order
        order_quantities = OrderQuantity.objects.filter(order=order)

        # Initialize a list to store the quantity for each dish in this order
        quantities_for_dishes = []

        for order_quantity in order_quantities:
            quantities_for_dishes.append({
                "dish_name": order_quantity.dish.dish_name,
                "quantity": order_quantity.quantity,
            })

        order_list.append({
            "cutomer_name": order.cutomer_name,
            "status": order.status,
            "quantities_for_dishes": quantities_for_dishes,
            "total_price": order.total_price
        })

    return JsonResponse({"orders": order_list})

def get_delivered_orders(request):
    if request.method == 'GET':
        delivered_orders = DeliveredOrder.objects.all()

        # Serialize the delivered orders to JSON
        orders_data = [
            {
                'order_id': order.order_id,
                'order_price': str(order.order_price),
                'customer_name': order.customer_name,
            }
            for order in delivered_orders
        ]

        return JsonResponse({'delivered_orders': orders_data})

    return JsonResponse({'message': 'Invalid request method'}, status=405)
