from django.shortcuts import render
from .models import HomeContent

# Create your views here.
def home(request):
    ctx = HomeContent.objects.get(contentId=1234)
    return render(request, 'index.html', {'data':ctx})

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def support(request):
    return render(request, 'support.html')