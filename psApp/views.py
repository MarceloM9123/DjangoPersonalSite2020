from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'psApp/dashboard.html')


def blog(request):
    return render(request, 'psApp/blog.html')


def products(request):
    return render(request, 'psApp/products.html')