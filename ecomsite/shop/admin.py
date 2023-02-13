from django.contrib import admin
from .models import Products,Order
# Register your models here.

# shoe Products model in the admin panel
admin.site.register(Products)
admin.site.register(Order)
