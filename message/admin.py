from django.contrib import admin
from message.models import  ContactMessage, FAQ ,subscrib

# Register your models here.
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name','subject', 'update_at','status']
    readonly_fields =('name','subject','email','message','ip')
    list_filter = ['status']

class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer','ordernumber','status']
    list_filter = ['status']
class subscribAdmin(admin.ModelAdmin):
    list_display = ['email']
    list_filter = ['email']


admin.site.register(ContactMessage,ContactMessageAdmin)
admin.site.register(FAQ,FAQAdmin) 
admin.site.register(subscrib,subscribAdmin)    