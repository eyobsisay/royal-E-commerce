import json
from django.http import JsonResponse
from django.contrib import messages
from account.decorators import login_required 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Avg, Count, Q, F
from django.db.models.functions import Concat
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import translation
from home.forms import SearchForm
from home.models import Setting, SliderImage,showroom
from Royal_market import settings
from shop.models import Category, product, image,  Variants ,Comment 
from django.db.models import Q
# from user.models import UserProfile
def try1(request):
    template_name='loginheader.html'
    companyinfo=Setting.objects.get(pk=2)
    context={
             
             'companyinfo':companyinfo,
             }

    return render(request,template_name,context)
@login_required(login_url='account_login')
def index(request):
    template_name = 'index.html'
    current_user = request.user
    products_latest = product.objects.all().order_by('-id')[:4]  # last 4 products
    products_slider = product.objects.all().order_by('id')[:4]  #first 4 products
    products_picked = product.objects.all().order_by('?')[:4]   #Random selected 4 products
    slider_image=SliderImage.objects.filter(is_active=True)
    
    # category =Category.objects.filter(level=0).order_by('id')
    category = Category.objects.all()
    page="home"
    context={
             'page':page,
             'products_slider': products_slider,
             'products_latest': products_latest,
             'products_picked': products_picked,
             'slider_image':slider_image,
             'category':category,
             'current_user':current_user,
             }
    return render(request,template_name,context)

def category_products(request,id,slug):
    template_name = 'product_category.html'
    catdata = Category.objects.get(pk=id)
    category = Category.objects.all()
    products = product.objects.filter(category_id=id) #default language
    if not products:
        productd =[]
        category=Category.objects.filter(parent_id=id)
        maincategory =Category.objects.filter(level=0).order_by('id')
        products =product.objects.filter(category_id__in=[rs.id for rs in category])
    category = Category.objects.all()
    context={'products': products,
             'catdata': catdata,
             'category': category,}
    return render(request,template_name,context)

def product_detail(request,id,slug):
    template_name = 'product_detail.html'
    query = request.GET.get('q')
    category = Category.objects.all()
    current_user = request.user
    products = product.objects.get(pk=id)
    related_product = product.objects.filter(title__icontains=products.title)
    images = image.objects.filter(product_id=id)
    context = {'products': products,'category': category,
               'images': images,'related_product':related_product,
               }
    if products.variant !="None": # Product have variants
        if request.method == 'POST': #if we select color
            variant_id = request.POST.get('variantid')
            variant = Variants.objects.get(id=variant_id) #selected product by click color radio
            colors = Variants.objects.filter(product_id=id,size_id=variant.size_id )
            sizes = Variants.objects.raw('SELECT * FROM  shop_variants  WHERE product_id=%s GROUP BY size_id',[id])
            query += variant.title+' Size:' +str(variant.size) +' Color:' +str(variant.color)
        else:
            variants = Variants.objects.filter(product_id=id)
            colors = Variants.objects.filter(product_id=id,size_id=variants[0].size_id )
            sizes = Variants.objects.raw('SELECT * FROM  shop_variants  WHERE product_id=%s GROUP BY size_id',[id])
            variant =Variants.objects.get(id=variants[0].id)
        context.update({'sizes': sizes, 'colors': colors,
                         'variant': variant,'query': query
                        })
    return render(request,template_name,context)

def ajaxcolor(request):
    data = {}
    if request.POST.get('action') == 'post':
        size_id = request.POST.get('size')
        productid = request.POST.get('productid')
        colors = Variants.objects.filter(product_id=productid, size_id=size_id)
        context = {
            'size_id': size_id,
            'productid': productid,
            'colors': colors,
        }
        data = {'rendered_table': render_to_string('color_list.html', context=context)}
        return JsonResponse(data)
    return JsonResponse(data)  
def search(request):
    template_name = 'search_result.html'
    if request.method == 'GET': # check post                
        # form = SearchForm(request.POST)
        query = request.GET.get("query", None)
        catid = request.GET.get("catid", None)
        print(catid)
        if query is not None:
            # query = form.cleaned_data['query'] # get form input data
            # catid = form.cleaned_data['catid']
            if catid=='0':
                products=product.objects.filter(title__icontains=query)  #SELECT * FROM product WHERE title LIKE '%query%'
                # product_catgory_id=products.values_list('category_id')
                # print('id=',product_catgory_id)
                relatedcatagory=Category.objects.filter(title__icontains=query)
            else:
                q=Category.objects.filter(Q(id=catid) | Q(parent_id=catid))
                
                print('q=',q)
                products = product.objects.filter(title__icontains=query,category_id__in=[rs.id for rs in q])
                relatedcatagory=Category.objects.filter(parent_id=catid)

            category = Category.objects.all()
            
            context = {'products': products, 'query':query,
                       'category': category,
                       'relatedcatagory':relatedcatagory, }        
            return render(request, template_name, context)

    return HttpResponseRedirect('/')

def search_auto(request):
    
    if request.is_ajax():
        q = request.GET.get('term', '')
        products = product.objects.filter(title__icontains=q)
        
        results = []
        for rs in products:
            product_json = {}
            product_json =rs.title 
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail a'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)      
# def showroom(requst):
#     show_room = showroom.object.all().order_by('-id')
#     context={
#         'showroom':show_room,
#     }
#     return render(request, template_name,context)
def aboutus(request):
    template_name = 'aboutus.html'
    current_user = request.user
    products_latest = product.objects.all().order_by('-id')[:4]  # last 4 products
    products_slider = product.objects.all().order_by('id')[:4]  #first 4 products
    products_picked = product.objects.all().order_by('?')[:4]   #Random selected 4 products
    page="home"
    context={
             'page':page,
             'current_user':current_user,
             }
    return render(request, template_name,context)
def contactus(request):
    template_name = 'contact_us.html'
    current_user = request.user
    context={
             'current_user':current_user,
             }

    return render(request, template_name,context)