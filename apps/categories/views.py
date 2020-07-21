from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Category
from .forms import CategoryForm

# Create your views here.
def category_list(request):
    categorys = Category.objects.all()
    context = {'categorys':categorys}
    return render(request, 'categories/category_list.html', context)

def category_create(request):
    form = CategoryForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy(category_list))
    return render(request, 'categories/category_create.html', context)

def product_update(request):
    category = Category.objects.get(id=request.GET['id'])
    form = CategoryForm(request.POST or None, instance=product)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('category_list'))
    if product:
        return render(request, 'categories/category_update.html', context)
    return redirect(reverse_lazy('category_list'))
