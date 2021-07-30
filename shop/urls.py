from django.conf.urls import url
from django.urls import include, path
from shop.views import index,product,chart,navbar,checkout,home

urlpatterns = [
    path('', home, name='home'),
    path('product/',product, name='product'),
    path('chart/',chart,name='chart'),
    path('navbar', navbar,name='navebar'),
    path('checkout', checkout,name='checkout'),
    path('index', index,name='index'),
  
    # url('recurit/',recurit, name='recurit'), # Notice the URL has been named
    
]
