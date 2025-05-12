from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import re

@csrf_exempt
def index(request):
    return render(request, 'home/index.html')

@csrf_exempt
def product1(request):
    return render(request, 'home/product1.html')

@csrf_exempt
def product2(request):
    return render(request, 'home/product2.html')

@csrf_exempt
def contact(request):
    return render(request, 'home/contact.html')

@csrf_exempt
def cart(request):
    cart_items = request.session.get('cart', [])
    total_price = request.session.get('total_price', 0)
    return render(request, 'home/cart.html', {'cart_items': cart_items, 'total_price': total_price})

@csrf_exempt
def payment(request):
    total_price = request.session.get('total_price', 0)
    phone = request.session.get('phone', '')
    return render(request, 'home/payment.html', {'total_price': total_price, 'phone': phone})

@csrf_exempt
def reviews(request):
    return render(request, 'home/reviews.html')