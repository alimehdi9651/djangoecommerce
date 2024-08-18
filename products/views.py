from django.shortcuts import render, redirect, get_list_or_404
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.
def category_list(request):
    return render(
        request, 'products/category_list.html',{
            'cateogries' : Category.objects.all(),
            'form' : CategoryForm()
        }
    )
def category_create(request):
    form = CategoryForm(request.POST, request.FILES)
    if form.is_valid():
        messages.success(request, 'Cateogry created successfully')
        form.save()
    else:
        messages.error(request, 'Error creating cateogry')
    return redirect('category_list')