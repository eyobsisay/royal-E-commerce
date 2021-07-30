from currencies.models import Currency
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from home.models import Language

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=50)
    image = models.ImageField(blank=True, upload_to='images/users/')
    # language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True,blank=True)
    # currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True,blank=True)


    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + ' [' + self.user.username + '] '

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


class Shippingaddres(models.Model):
    title = models.CharField(blank=True, max_length=20)
    first_name  = models.CharField(blank=True, max_length=20)
    email = EmailField(max_length=254, blank=True)
    last_name  = models.CharField(blank=True, max_length=20)
    telephone =PhoneNumberField()
    telephone2=PhoneNumberField()
    company  = models.CharField(blank=True, max_length=20)
    addres_1  = models.CharField(blank=True, max_length=20)
    addres_2  = models.CharField(blank=True, max_length=20)
    city = models.CharField(blank=True, max_length=20)
    postcode =models.CharField(blank=True, max_length=20)
    country =CountryField(multiple=False)
    region = CountryField(multiple=False)
    class Meta:
        verbose_name = "Shipping addres"
        verbose_name_plural = "Shipping addres"

    def __str__(self):
        pass


    
class billing_address(models.Model):
    first_name= models.CharField(blank=True, max_length=20)
    last_name = models.CharField(blank=True, max_length=20)
    email = models.EmailField(max_length=254, blank=True)
    address = models.CharField(blank=True, max_length=20)
    addres_1  = models.CharField(blank=True, max_length=20)
    addres_2  = models.CharField(blank=True, max_length=20)
    city = models.CharField(blank=True, max_length=20)
    zipcode = models.CharField(blank=True, max_length=20)
    telephone =PhoneNumberField()
    telephone2=PhoneNumberField()
    country =CountryField(multiple=False)
    region = cCountryField(multiple=False)
    class Meta:
        verbose_name = "Billing Address"
        verbose_name_plural = "BILLING ADDRESS"

    def __str__(self):
        pass
 
# class recioientsaddres(models.Model):
#     name
#     phoneno
#     otherphonno
#     country = CountryField(multiple=False)
#     streetname
#     housenumber
#     city
#     area
#     subvity
#     email
#     class Meta:
#         verbose_name = "recioients addres"
#         verbose_name_plural = "recioientss"

#     def __str__(self):
#         pass