from django import template
from cart.models import Cart, CartItem

# create a object of Library class
register = template.Library() #This creates an object register that is used to register custom template tags. Django uses this to recognize the cart_item_count function as a custom tag that can be used in templates.

# create a custom template tag
@register.simple_tag(takes_context=True)
def cart_item_count(context):
    request = context['request']
    if 'cart' in request.session:
        return request.session['cart']
    else:
        # count items in cart
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            no_of_items = cart.cartitem_set.count()
            request.session['cart'] = no_of_items
            return no_of_items
        return 0