from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'products/product_list.html', context)

def product_create(request):
    form = ProductForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('product_list'))
    return render(request, 'products/product_create.html', context)
