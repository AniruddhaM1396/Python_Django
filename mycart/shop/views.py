from urllib import response
from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    #return HttpResponse("index enetered")
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    return render(request, 'shop/index.html', params)
    
def about(request):
    #return HttpResponse("index enetered")
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("index enetered")
    #return render(request,'shop/index.html')

def productview(request):
    return HttpResponse("index enetered")
    #return render(request,'shop/index.html')

def tracker(request):
    return HttpResponse("index enetered")
    #return render(request,'shop/index.html')

def checkout(request):
    return HttpResponse("index enetered")
    #return render(request,'shop/index.html')

def search(request):
    return HttpResponse("index enetered")
    #return render(request,'shop/index.html')

