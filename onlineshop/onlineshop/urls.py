"""onlineshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from shop import views
from django.conf.urls.static import static
import settings

urlpatterns = [
    url(r'^add_product/(?P<pk>\d+)/$',views.AddProduct.as_view(),name='addproduct'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^detail/(?P<product_id>\d+)$', views.Details.as_view(), name='detail'),
    url(r'^shoppingcart/$', views.shopping_cart, name='shoppingcart'),

]+ static('Pictures/', document_root=settings.UPLOAD_ROOT)
