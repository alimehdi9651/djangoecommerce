from django.shortcuts import render, redirect

# Create your views here.
def show_cart(request):
    return render(request, 'cart/show.html')
def success(request):
    return render(request, 'cart/success.html')
def failure(request):
    return render(request, 'cart/failure.html')
def order(request):
    return render(request, 'cart/order.html')
def add_product(request):
    referrer = request.META.get('HTTP_REFERER')
    return redirect(referrer)
def remove_product(request):
    referrer = request.META.get('HTTP_REFERER')
    return redirect(referrer)
def increase_qty(request):
    referrer = request.META.get('HTTP_REFERER')
    return redirect(referrer)
def decrease_qty(request):
    referrer = request.META.get('HTTP_REFERER')
    return redirect(referrer)

