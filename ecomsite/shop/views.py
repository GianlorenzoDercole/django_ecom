from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator
# Create your views here.

# view for homepage which will display index.html template
def index(request):
    product_objects = Products.objects.all()

    item_name = request.GET.get('item_name')
    # search products for item added to search bar
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

    # paginator
    paginator = Paginator(product_objects,2)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request,'shop/index.html',{'product_objects':product_objects})
