from django.urls import path
from .import views

urlpatterns = [
    path('show', views.show_cart, name = 'show_cart'),
    path('add/<slug:product>', views.add_product, name = 'add_cart'),
    path('remove/<slug:product>', views.remove_product, name = 'remove_cart'),
    path('remove/<slug:product>', views.remove_product, name = 'increase_qty'),
    path('remove/<slug:product>', views.remove_product, name = 'decrease_qty'),
    path('checkout', views.checkout, name='checkout'),
    path('success/', views.success, name='success'),
    path('failure/', views.failure, name='failed'),
    path('orders/', views.orders, name='orders'),
    
]