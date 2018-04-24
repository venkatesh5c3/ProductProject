from django.db import models


# Create your models here.


class Product(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=20)
    pdate = models.DateField(default='01-01-2018')


class Menu(models.Model):
    menuId = models.IntegerField(primary_key=True)
    menuName = models.CharField(max_length=20)


class Item(models.Model):
    itemId = models.IntegerField(primary_key=True)
    itemName = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
