from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
def home(request):
    template_name = 'store.html'

    return render(request, template_name)
def index(request):
    template_name = 'index.html'

    return render(request, template_name)
def product(request):
	template_name = 'product_detail.html'
	return render(request, template_name)

def chart(request):
	template_name= 'chart.html'
	return render(request,template_name)

def navbar(request):
	template_name='navbar.html'
	return render(request,template_name)

def checkout(request):
    template_name='checkout.html'
    return render(request,template_name)