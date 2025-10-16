from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=100)
    stock_amount = models.PositiveIntegerField()
    stock_price = models.PositiveIntegerField()


class SaleRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    price = models.PositiveIntegerField()


class BuyRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
