from django.db import models
from django.http.response import HttpResponse
from django.shortcuts import render
from pages.views import navbar_context
from .models import Product
import operator
import re

# Create your views here.
def products_view(request):
    page_no = 1
    max_ = 13 * page_no
    all_products = Product.objects.all()
    page_products = all_products.order_by("id")

    if request.method == 'POST':
        

        sort = request.POST.get('sort')
        print(sort)
        if sort == 'default':
            page_products = all_products.order_by("id")
        elif sort == 'price':
            print("ok")
            page_products = all_products.order_by("price")
        elif sort == '!price':
            page_products = all_products.order_by("-price")
        elif sort == 'alpha':
            page_products = all_products.order_by("name")
        elif sort == '!alpha':
            page_products = all_products.order_by("-name")
    
    page_products = page_products[:max_]
    
    context = {}
    for i, model in enumerate(page_products):
        context["p" + str(i + 1)] = model

    context.update(navbar_context)
    
    return render(request, "products.html", context)

def product_details(request):
    no_of_prod = len(Product.objects.all())
    full_path = str(request.get_full_path())
    pid = int(re.search('[0-9]+$', full_path).group(0))
    print(full_path, type(pid))
    
    products = list(Product.objects.all()[pid-1:pid+4])
    if (pid+4 > no_of_prod):
        excess = pid+4 - no_of_prod
        products += list(Product.objects.all()[0:excess+1])
    
    context = {}
    
    for i, model in enumerate(products):
        context["p" + str(i + 1)] = model
    
    context.update(navbar_context)
    return render(request, "productdetails.html", context)