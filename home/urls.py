from django.conf.urls import url
from django.urls import include, path
from home.views import index ,product_detail,ajaxcolor,search,search_auto,category_products,try1,aboutus,contactus


urlpatterns = [
    path('', index, name='home'),
    path('product/<int:id>/<slug:slug>/', product_detail, name='product_detail'),
    path('ajaxcolor/', ajaxcolor, name='ajaxcolor'),
    path('search/', search, name='search'),
    path('search_auto/', search_auto, name='search_auto'),
    path('category/<int:id>/<slug:slug>', category_products, name='category_products'),
    path('try', try1, name='try1'),
    path('about_us',aboutus, name='aboutus'),
    # path('contact_us',contactus,name='contactus')


  
  
    # url('recurit/',recurit, name='recurit'), # Notice the URL has been named
    
]
