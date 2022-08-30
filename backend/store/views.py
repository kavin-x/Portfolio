from django.shortcuts import render
from .models import Category,Product
# Create your views here.
def allProducts(request):
    product=Product.objects.all()
    print(product)
    return render(request,'store/home.html',{'product':product})
