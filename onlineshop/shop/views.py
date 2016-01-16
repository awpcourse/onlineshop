from django.shortcuts import render

from django.views.generic import TemplateView
from models import Product
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from shop.forms import UserLoginForm, UserRegisterForm


class Home(TemplateView):
    template_name = "home.html"

    def get_user(self):
        username = None
        if self.request.user.is_authenticated():
            username = self.request.user.username
            return username

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