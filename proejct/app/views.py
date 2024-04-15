from django.shortcuts import render

def home(req):
    return render(req,'app/home.html')

def about(req):
    return render(req,'app/about.html')

def contact(req):
    return render(req,'app/contact.html')

def products(req):
    return render(req,'app/products.html')


def cart(req):
    return render(req,'app/cart.html')
