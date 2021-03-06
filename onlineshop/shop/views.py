from django.shortcuts import render
from django.db.models import Sum
from django.views.generic import TemplateView
from models import Product, History
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from shop.forms import UserLoginForm, UserRegisterForm
from shop.forms import UserLoginForm
from shop.models import CommandLine, ProductComment
from django.views.generic.list import ListView
from django.http import HttpResponse

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View
from .forms import CommentForm


class Home(TemplateView):
    template_name = "home.html"

    def get_user(self):
        username = None
        if self.request.user.is_authenticated():
            username = self.request.user.username
            return username

    def list_products(self):
        return Product.objects.all()

class Details(View):
    template_name = "detail.html"
    form_class = CommentForm

    def get_product(self):
        return Product.objects.get(id=self.kwargs['product_id'])

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        product = Product.objects.get(id=self.kwargs['product_id'])
        comments = ProductComment.objects.filter(id_product=self.kwargs['product_id'])

        return render(request, self.template_name, {'form': form,'product': product, 'comments': comments})



    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            comment = ProductComment(text=text, id_user=request.user, id_product=Product.objects.get(id=self.kwargs['product_id']))
            comment.save()
            return self.get(request, *args, **kwargs)

        return render(request, self.template_name, {'form': form})





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
        try:
            new_product = CommandLine.objects.get(id_user = request.user)
        except ObjectDoesNotExist:
            new_product = CommandLine(id_user = request.user)
            new_product.save()
            new_product.id_products.add(self.kwargs['pk'])
            return redirect('/')
        try:
            new_product.id_products.add(self.kwargs['pk'])
            return redirect('/')
        except IntegrityError:
            return HttpResponse("Item already added!")

class DeleteProduct(ListView):
    model = CommandLine
    template_name = 'delete_product.html'
    def get(self, request, *arsg, **kwargs):
        cart = CommandLine.objects.get(id_user = request.user)
        cart.id_products.remove(self.kwargs['pk'])
        return redirect('/')

def shopping_cart(request):
    try:
        cart = get_cart(request)
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
    else:
        if request.method == 'POST':
            return confirm_order(request)


def get_cart(request):
    return CommandLine.objects.get(id_user = request.user)      

def confirm_order(request):
    cart=get_cart(request)
    history = History(id_user=request.user) 
    history.save() 
    for product in cart.id_products.all():
        product.quantity = product.quantity - 1
        history.id_product.add(product)
        product.save()
    history.save()
    cart.delete()    
    return redirect('home')
