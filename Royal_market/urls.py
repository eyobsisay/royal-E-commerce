"""Royal_market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from shop import urls as shop_urls
from home import urls as home_urls
from message import urls as message_urls
from home import views
from order import urls as order_urls
# from home.views import index,ajaxcolor
from shop.views import product,chart,navbar
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
urlpatterns = [
    # path('', include(home_urls)),
    path('admin/', admin.site.urls),
    path('shop/', include(shop_urls)),
    path('order/', include(order_urls)),
    path("account/", include("account.urls")),
    path('search/', views.search, name='search'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('home/', include("home.urls")),
    path('message/',include('message.urls')),
     # path('', index, name='royal'),
    # path('account/', include("account.urls")),
     # path('imagefit/', include('imagefit.urls')),
    
]
urlpatterns += i18n_patterns(
    
    path('ckeditor/', include('ckeditor_uploader.urls')),


   
    
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)