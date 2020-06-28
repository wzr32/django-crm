from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import *

# Create your views here.

def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_orders = orders.all().count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {
        'customers': customers,
        'orders': orders,
        'delivered': delivered,
        'pending': pending,
        'total_orders': total_orders
    }
    return render(request, 'accounts/dashboard.html', context)


def product(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'accounts/products.html', context)


def customer(request, id):
    customer = Customer.objects.get(id=id)
    orders = customer.order_set.all()
    context = {
        'customer': customer,
        'orders': orders
    }
    return render(request, 'accounts/customer.html', context)

def create_order(request, id):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=5)
    customer = Customer.objects.get(id=id)
    form_set = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == 'POST':
        form_set = OrderForm(request.POST)
        if form_set.is_valid():
            form_set.save()
        return redirect('home')
    context = {
        'form_set': form_set
    }
    return render(request, 'accounts/order_form.html', context)

def update_order(request,id):
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'accounts/order_form.html', context)

def delete_order(request, id):
    order = Order.objects.get(id=id)
    if request.method == 'POST':
        order.delete()
        return redirect('home')
    context = {
        'order': order
    }
    return render(request,'accounts/delete.html', context) 