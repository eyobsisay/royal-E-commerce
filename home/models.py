from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput, Textarea
from django.http import request
from django.utils.safestring import mark_safe
from phonenumber_field.modelfields import PhoneNumberField
# class Language(models.Model):
#     name= models.CharField(max_length=20)
#     code= models.CharField(max_length=5)
#     status=models.BooleanField()
#     create_at=models.DateTimeField(auto_now_add=True)
#     update_at=models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name

# llist = Language.objects.filter(status=True)
# list1 = []
# for rs in llist:
#     list1.append((rs.code,rs.name))
# langlist = (list1)
class SliderImage(models.Model):
    slider_image = models.ImageField(blank=True,upload_to='slider_image/' ,verbose_name='Slider Image')
    caption1= models.CharField(max_length=500,verbose_name='Caption')
    caption2= models.CharField(max_length=500,verbose_name='Caption')
    description=models.CharField(max_length=500,verbose_name='Description')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Slider Image"
        verbose_name_plural = "Slider Images"

    def image_tag(self):
        if self.slider_image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.slider_image.url))
        else:
            return ""  
    def __str__(self):
        return self.caption1
    
class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150 )
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True,max_length=100)
    phone = models.CharField(blank=True,max_length=15)
    fax = models.CharField(blank=True,max_length=15)
    email = models.CharField(blank=True,max_length=50)
    smtpserver = models.CharField(blank=True,max_length=50)
    smtpemail = models.CharField(blank=True,max_length=50)
    smtppassword = models.CharField(blank=True,max_length=10)
    smtpport = models.CharField(blank=True,max_length=5)
    icon = models.ImageField(blank=True,upload_to='images/')
    facebook = models.CharField(blank=True,max_length=50)
    instagram = models.CharField(blank=True,max_length=50)
    twitter = models.CharField(blank=True,max_length=50)
    youtube = models.CharField(blank=True, max_length=50)
    aboutus = RichTextUploadingField(blank=True)
    Mission = RichTextUploadingField(blank=True)
    Vission = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status=models.CharField(max_length=10,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
class showroom(models.Model):
    title=models.CharField(max_length=100)
    keywords=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    phone1=PhoneNumberField()
    phone2=PhoneNumberField()

    class Meta:
        verbose_name = "showroom"
        verbose_name_plural = "showrooms"

    def __str__(self):
        return self.title
    

# class SettingLang(models.Model):
#     setting = models.ForeignKey(Setting, on_delete=models.CASCADE) #many to one relation with Category
#     lang =  models.CharField(max_length=6, choices=langlist)
#     title = models.CharField(max_length=150)
#     keywords = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     aboutus = RichTextUploadingField(blank=True)
#     contact = RichTextUploadingField(blank=True)
#     references = RichTextUploadingField(blank=True)
#     def __str__(self):
#         return self.title

class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name= models.CharField(blank=True,max_length=20)
    email= models.CharField(blank=True,max_length=50)
    subject= models.CharField(blank=True,max_length=50)
    message= models.TextField(blank=True,max_length=255)
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject','message']
        widgets = {
            'name'   : TextInput(attrs={'class': 'input','placeholder':'Name & Surname'}),
            'subject' : TextInput(attrs={'class': 'input','placeholder':'Subject'}),
            'email'   : TextInput(attrs={'class': 'input','placeholder':'Email Address'}),
            'message' : Textarea(attrs={'class': 'input','placeholder':'Your Message','rows':'5'}),
        }



class FAQ(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    # lang =  models.CharField(max_length=6, choices=langlist, blank=True, null=True)
    ordernumber = models.IntegerField()
    question = models.CharField(max_length=200)
    answer = RichTextUploadingField()
    status=models.CharField(max_length=10, choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question



