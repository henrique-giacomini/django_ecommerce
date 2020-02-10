from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

# Create your views here.

class ProductListView():
    queryset = Product.objects.all()
