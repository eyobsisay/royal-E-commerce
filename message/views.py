from django.shortcuts import render
from message.forms import ContactForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.shortcuts import render
from shop.models import Category, product, image,  Variants ,Comment
from home.models import Setting, ContactForm, ContactMessage, FAQ
from message.models import FAQ, ContactMessage,subscrib
from message.forms import ContactForm,subscribForm
from django.contrib import messages
from django.urls import reverse
# Create your views here.

def contactus(request):
    template_name = 'contact_us.html'
    contact_form=ContactForm
    SubscribForm = subscribForm
    current_user = request.user
    maincategory =Category.objects.filter(level=0).order_by('id')
    companyinfo=Setting.objects.get(pk=2)
    if request.method == 'POST': # check post
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage() #create relation with model
            data.name = form.cleaned_data['name'] # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  #save data to table
            messages.success(request,"Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect(reverse('contactus'))
    context={
             'maincategory':maincategory,
             'current_user':current_user,
             'companyinfo':companyinfo,
             'contact_form':contact_form,
             'subscribForm':SubscribForm,
             }

    return render(request, template_name,context)
def subscriber(request):
       if request.method == 'GET':
            if request.GET.get('subscriber_email'):
                subscribmodel=subscrib()
                subscribmodel.email=request.GET.get('subscriber_email')
                subscribmodel.save()
                messages.success(request,"SUBSCIBED SUCCESSFULY.")
                return HttpResponseRedirect(reverse('contactus'))

            else:
                return HttpResponseRedirect(reverse('home'))