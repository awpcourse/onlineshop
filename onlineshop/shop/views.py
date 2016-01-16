from django.shortcuts import render
from django.db.models import Sum
from django.views.generic import TemplateView
from models import Product
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from shop.forms import UserLoginForm
from shop.models import CommandLine
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

class Home(TemplateView):
    template_name = "home.html"
    def list_products(self):
        return Product.objects.all()


def login_view(request):
    if request.method == 'GET':
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'login.html', context)
    elif request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            context = {
                'form': form,
                'message': 'Wrong username or password!'
            }
            return render(request, 'login.html', context)
        else:
            login(request, user)
            return redirect('/')



class AddProduct(ListView):
    model = CommandLine
    template_name = 'add_product.html'
    
    def get(self, request, *args, **kwargs):

        new_product = CommandLine.objects.get(id_user = request.user)
        if new_product == None :
            new_product = CommandLine(id_user = request.user)
            new_product.save()
            new_product.id_products.add(self.kwargs['pk'])
        else :
            new_product.id_products.add(self.kwargs['pk'])
        return redirect('/')

def shopping_cart(request):
    try:
        cart = CommandLine.objects.get(id_user = request.user)
        products = cart.id_products.all()
    except ObjectDoesNotExist:
        products = []
    total = sum([p.price for p in products])
    if request.method == 'GET':
        context = {
            'products': products,
            'total' : total,
        }
        return render(request, 'shopping-cart.html', context)

    
    
    
    
        
