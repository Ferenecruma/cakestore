from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from webstore.models import Product
from .cart import Cart

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    response_data = {
                    'status' : 'success', 
                    'message' : 'added',
                    'items_num' : str(len(cart))}
    return JsonResponse(response_data)
 
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product=product)
    if request.is_ajax():
        response_data = {'status' : 'success', 'message' : 'removed'}
        return JsonResponse(response_data)
    else:
        return redirect('cart-main')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})
