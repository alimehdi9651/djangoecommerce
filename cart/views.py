from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from cart.models import Cart, CartItem, Order

from django.contrib.auth.decorators import login_required
from django.contrib import messages

def show_cart(request):
    return render(request, 'cart/show.html')

def success(request):
    return render(request, 'cart/success.html')

def failure(request):
    return render(request, 'cart/failure.html')

def orders(request):
    return render(request, 'cart/orders.html')

@login_required
def add_product(request, product):
    referrer = request.META.get('HTTP_REFERER')
    product = get_object_or_404(Product, slug=product)
    cart,_ = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created=CartItem.objects.get_or_create(cart=cart, product=product)
    print(cart_item, item_created)
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, 'Product quantity increased to cart')
    else:
        messages.success(request, 'Product added to cart')
    no_of_items = cart.cartitem_set.count()
    request.session['cart'] = no_of_items
    print(request.session['cart'], 'items')
    return redirect(referrer)

def remove_product(request, product):
    referrer = request.META.get('HTTP_REFERER')
    product = get_object_or_404(Product, slug=product)
    cart, _ = Cart.objects.get_or_create()
    return redirect(referrer)

def increase_qty(request, product):
    referrer = request.META.get('HTTP_REFERER')
    return redirect(referrer)

def decrease_qty(request, product):
    referrer = request.META.get('HTTP_REFERER')
    return redirect(referrer)

def checkout(request):
    pass
