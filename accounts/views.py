from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    context = {
        "customers": customers,
        "orders": orders,
    }

    return render(request, "accounts/dashboard.html", context)


def product(request):
    all_products = Product.objects.all()
    return render(request, "accounts/products.html", {"all_prod": all_products})


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()
    context = {'customer': customer, 'orders': orders, 'orders_count': orders_count}
    return render(request, "accounts/customer.html", context)

def create_order(request):
    return render(request, "accounts/order_form.html")