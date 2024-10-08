from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s cart"
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default = 1)

    def total_price(self):
        return self.product.price * self.quantity

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.BooleanField(default=False)
    is_deliverd = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default = False)
    address = models.TextField()
    razorpay_order_id = models.CharField(max_length=255, null = True, blank = True)
    razorpay_payment_id = models.CharField(max_length=255, null = True, blank = True)

    def __str__(self):
        return f"{self.product.title} - {self.user.username}"