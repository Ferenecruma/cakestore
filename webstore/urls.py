from django.urls import path
from  . import views


urlpatterns = [
    path('', views.home, name='store-main'),
    path('about', views.about, name='store-about'),
    path('category', views.category, name='store-category')
]