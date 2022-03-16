import django
from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import render

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})