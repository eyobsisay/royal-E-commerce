from django.conf.urls import url
from django.urls import include, path
from message.views import contactus,subscriber


urlpatterns = [
    path('contact_us',contactus,name='contactus'),
    path('subscriber',subscriber,name='subscriber')


  
  
    # url('recurit/',recurit, name='recurit'), # Notice the URL has been named
    
]
