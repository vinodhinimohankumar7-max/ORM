from django.db import models
from django.contrib import admin
class Product(models.Model):
    serialNo= models.CharField(primary_key=True,max_length=8)
    ProductName=models.CharField(max_length=30)
    ManufactureDate=models.DateTimeField()
    Price=models.IntegerField()
    Quantity=models.IntegerField()
class ProductAdmin(admin.ModelAdmin):
    list_display=["serialNo","ProductName","ManufactureDate","Price","Quantity"]