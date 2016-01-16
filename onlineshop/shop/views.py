from django.shortcuts import render

from django.views.generic import TemplateView
from models import Product
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from shop.forms import UserLoginForm

class Home(TemplateView):
    template_name = "home.html"
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
