from django.db import models
from shop.models import Book
from django.contrib.auth.models import User

class Cart(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.book.name
    def subtotal(self):
        return self.quantity*self.book.price
class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_items = models.IntegerField()
    address=models.TextField()
    phone=models.CharField(max_length=30)
    order_status=models.CharField(max_length=20,default="pending")
    delivery_status=models.CharField(max_length=20,default="pending")
    date_ordered=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

class Account(models.Model):
    acctnum=models.CharField(max_length=20)
    accttype=models.CharField(max_length=20)
    amount=models.IntegerField()
    amount=models.IntegerField()
    def __str__(self):
        return self.acctnum




