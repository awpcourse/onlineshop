from django.shortcuts import render
from django.db.models import Sum
from django.views.generic import TemplateView
from models import Product
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from shop.forms import UserLoginForm, UserRegisterForm
from shop.forms import UserLoginForm
from shop.models import CommandLine
from django.views.generic.list import ListView
from django.http import HttpResponse


class Home(TemplateView):
    template_name = "home.html"

    def get_user(self):
        username = None
        if self.request.user.is_authenticated():
            username = self.request.user.username
            return username

    def list_products(self):
        return Product.objects.all()

class Details(TemplateView):
    template_name = "detail.html"
    def get_product(self):
        return Product.objects.get(id=self.kwargs['product_id'])

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

def logout_view(request):
    logout(request)
    return redirect('login')            

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {
        'form': form,
    })


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
    products = CommandLine.objects.get(id_user = request.user)
    total = sum([p.price for p in products.id_products.all()])
    if request.method == 'GET':
        context = {
            'products': products,
            'total' : total,
        }
        return render(request, 'shopping-cart.html', context)
