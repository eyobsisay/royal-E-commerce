from django.urls import path

from order.views import shopcart,addtoshopcart,deletefromcart,index,cheakout,addtowhishlist,whishlist,deletefromwhishcart

urlpatterns = [
    path('', index, name='index'),
    path('addtoshopcart/<int:id>', addtoshopcart, name='addtoshopcart'),
    path('addtowhishlist/<int:id>', addtowhishlist, name='addtowhishlist'),
    path('deletefromcart/<int:id>',deletefromcart, name='deletefromcart'),
    path('deletefromwhishcart/<int:id>',deletefromwhishcart, name='deletefromwhishcart'),
    path('shopcart/', shopcart, name='shopcart'),
    path('whishlist/', whishlist, name='whislist'),
    path('checkout',cheakout,name='checkout'),

    # path('orderproduct/', views.orderproduct, name='orderproduct'),
]

