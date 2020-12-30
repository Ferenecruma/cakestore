from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="store-main"),
    path("fetch_main", views.get_main_content, name="fetch-main"),
    path("about", views.about, name="store-about"),
    path("categories", views.catagories, name="store-categories"),
    path("category/<slug:slug>/", views.category, name="store-category"),
]
