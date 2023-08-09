from django.shortcuts import render, redirect
import random
from django.urls import path

app_name = 'crud'

items = []

def index(request):
    return render(request, 'crud/index.html', {'items': items})

def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        new_item = {'name': name, 'email': email, 'id': len(items)}
        items.append(new_item)
        return redirect('crud:home')
    return render(request, 'crud/create.html')

def update(request, item_id):
    item = items[item_id]
    
    if request.method == 'POST':
        item['name'] = request.POST['name']
        item['email'] = request.POST['email']
        return redirect('crud:home')
    
    return render(request, 'crud/update.html', {'item': item})

def delete(request, item_id):
    items.pop(item_id)
    return redirect('crud:home')
