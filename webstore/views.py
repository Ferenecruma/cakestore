from django.shortcuts import render
from django.http import HttpResponse

cakes = [
    {
        'name' : 'chocolate',
        'price' : '1999',
        'weight' : '2kg',

    },
    {
        'name' : 'pancake',
        'price' : '3000',
        'weight' : '1kg',

    }
]

for _ in range(3):
    cakes += cakes
cakes = cakes[:6]

def home(request):
    context = {
        'cakes' : cakes
    }
    return render(request, 'webstore/home.html', context)

def about(request):
    return render(request, 'webstore/about.html')

def category(request):
    return render(request, 'webstore/category.html')
