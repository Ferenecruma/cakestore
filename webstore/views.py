from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product, SubCategory


def home(request):
    return render(request, 'webstore/home.html')

def about(request):
    return render(request, 'webstore/about.html')

def get_main_content(request):
    print("returning content")
    return render(request, 'webstore/main-content.html')

def catagories(request):
    context = dict()
    context['categories'] = get_main_categories()
    return render(request, 'webstore/categories.html', context)

def category(request, slug):
    products = get_products_by_category(slug)
    subcategories = SubCategory.objects.filter(category__slug=slug)
    return render(request, 'webstore/category.html', {
        'products' : products,
        'subcategories' : subcategories,
    })

def get_main_categories():
    main_categories = Category.objects.all()
    return main_categories

def get_products_by_category(slug):
    products = Product.objects.filter(category__slug=slug)
    return products
