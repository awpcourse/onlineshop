from django.shortcuts import render
from django.views.generic import TemplateView
from models import Product
# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
    def list_products(self):
        return Product.objects.all()
