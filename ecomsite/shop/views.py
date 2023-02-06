from django.shortcuts import render
from .models import Products
# Create your views here.

# view for homepage which will display index.html template
def index(request):
    product_objects = Products.objects.all()
    return render(request,'shop/index.html',{'product_objects':product_objects})
