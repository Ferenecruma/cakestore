from django.urls import path
from  . import views


urlpatterns = [
    path('', views.cart_detail, name='cart-main'),
    path('add/<int:product_id>/', views.cart_add, name='cart-add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart-remove'),
]