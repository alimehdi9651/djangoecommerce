from django.urls import path
from .views import *

urlpatterns = [
    path('category/', category_list, name='category_list'),
    path('category/create/', category_create, name='category_create'),
    path('category/edit/<slug:slug>/', category_list, name='category_edit'),
    path('category/delete/<slug>', category_list, name='category_list'),
]