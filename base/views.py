from unicodedata import name
from django.shortcuts import render
# Create your views here.


products = [
    {'id': 1 , 'name': 'Hoodie', 'price': 50, 'seller': 'admin', 'category': 'Clothing' },
    {'id': 2 , 'name': 'Hoodie', 'price': 100, 'seller': 'admin', 'category': 'Clothing' },
    {'id': 3 , 'name': 'Hoodie', 'price': 150, 'seller': 'admin', 'category': 'Clothing' },
]

def home(request):
    context = {'products': products}
    return render(request, 'index.html', context)