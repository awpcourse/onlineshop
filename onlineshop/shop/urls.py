from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import patterns
from app import views

urlpatterns = patterns('',
    
    url(r'^login/$', views.login_view, name='login'),
)