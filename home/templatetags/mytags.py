from django import template
from django.db.models import Sum
from django.urls import reverse

from Royal_market import settings
from order.models import ShopCart, Whishlist
from shop.models import Category
from home.models import showroom,Setting


register = template.Library()


@register.simple_tag
def shopcartcount(userid):
    count = ShopCart.objects.filter(user_id=userid).count()
   
    return count 
@register.simple_tag
def shopcartlist(userid):
     cartlist =ShopCart.objects.filter(user_id=userid)
     return cartlist
@register.simple_tag     
def shopcarttotal(userid):
    shopcart =ShopCart.objects.filter(user_id=userid)
    total=0
    for rs in shopcart:
        total += rs.price * rs.quantity

    return total
# wishlist
@register.simple_tag
def wishlistcount(userid):
    count = Whishlist.objects.filter(user_id=userid).count()
   
    return count 
@register.simple_tag
def wishlistlist(userid):
     cartlist =Whishlist.objects.filter(user_id=userid)
     return cartlist
@register.simple_tag     
def wishlisttotal(userid):
    Whishlisttot =Whishlist.objects.filter(user_id=userid)
    total=0
    for rs in Whishlisttot:
        total += rs.price * rs.quantity

    return total

@register.simple_tag
def categoryTree(id,menu,lang):
    defaultlang = settings.LANGUAGE_CODE[0:2]
    #lang='tr'
    
    query = Category.objects.raw('SELECT c.id,l.title, l.keywords, l.description,l.slug'
                                 '  FROM product_category as c'
                                 '  INNER JOIN product_categorylang as  l'
                                 '  ON c.id = l.category_id'
                                 '  WHERE  parent_id =%s AND lang=%s', [id,lang])
    querycount = Category.objects.filter(parent_id= id).count()
    if querycount > 0:
        for rs in query:
            subcount = Category.objects.filter(parent_id=rs.id).count()
            if subcount > 0:
                menu += '\t<li class="dropdown side-dropdown">\n'
                menu += '\t<a class ="dropdown-toggle" data-toggle="dropdown" aria-expanded="true">'+ rs.title +'<i class="fa fa-angle-right"></i></a>\n'
                menu += '\t\t<div class="custom-menu">\n'
                menu += '\t\t\t<ul class="list-links">\n'
                menu += categoryTree(int(rs.id),'',lang)
                menu += '\t\t\t</ul>\n'
                menu += '\t\t</div>\n'
                menu += "\t</li>\n\n"
            else :
                menu += '\t\t\t\t<li><a href="'+reverse('category_products',args=(rs.id, rs.slug)) +'">' + rs.title + '</a></li>\n'
    return menu    
# showroom list in all page
@register.simple_tag
def showroomlist():
    show_room_list = showroom.objects.all()

    return show_room_list
@register.simple_tag
def maincategorylist():
    maincategory =Category.objects.filter(level=0).order_by('id')

    return maincategory_list    
@register.simple_tag
def companyinfo():
    companyinfo=Setting.objects.get(pk=2)

    return companyinfo    
companyinfo=Setting.objects.get(pk=2)
# main Category below the navbare
@register.simple_tag
def maincategorylist():
     maincategory_list =Category.objects.filter(level=0).order_by('id')

     return maincategory_list