from django.urls import path
from . import views

#MVT (Model Views Template)
app_name = 'sapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('about', views.about, name='about'),
    path('support', views.support, name='support'),
    path('contact', views.contact, name='contact'),
]