from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'menu.html')


def order(request):
    return render(request, 'orders.html')
