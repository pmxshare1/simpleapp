from django.urls import path
from . import views

#MVT (Model Views Template)

urlpatterns = [
    path('', views.home, name='home')
]