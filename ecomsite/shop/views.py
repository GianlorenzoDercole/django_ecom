from django.shortcuts import render
from .models import Products,Order
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
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request,'shop/index.html',{'product_objects':product_objects})

# view for detail of a product
def detail(request,id):
    product_object = Products.objects.get(id=id)
    return render(request,'shop/detail.html',{'product_object':product_object})
# view for checkout page
def checkout(request):

    if request.method == 'POST':
        items = request.POST.get('items','')
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"")

        order = Order(items=items,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode,total=total)
        order.save()

    return render(request,'shop/checkout.html')
