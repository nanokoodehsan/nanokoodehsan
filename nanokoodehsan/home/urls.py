from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.index, name='index'),
    path('product1/', views.product1, name='product1'),
    path('product2/', views.product2, name='product2'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('payment/', views.payment, name='payment'),
    path('reviews/', views.reviews, name='reviews'),
]