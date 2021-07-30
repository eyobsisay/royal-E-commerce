from django.contrib import admin

# Register your models here.
from home.models import Setting,showroom,SliderImage

class SliderImageAdmin(admin.ModelAdmin):
    list_display = ['id','caption1','caption2', 'description','is_active','image_tag']

class SettingtAdmin(admin.ModelAdmin):
    list_display = ['title','company', 'update_at','status']

# class ContactMessageAdmin(admin.ModelAdmin):
#     list_display = ['name','subject', 'update_at','status']
#     readonly_fields =('name','subject','email','message','ip')
#     list_filter = ['status']

# class FAQAdmin(admin.ModelAdmin):
#     list_display = ['question', 'answer','ordernumber','status']
#     list_filter = ['status']
class showroomAdmin(admin.ModelAdmin):
    list_display=['title','keywords','address','phone1','phone2']
    list_filter = ['title']

# class LanguagesAdmin(admin.ModelAdmin):
#     list_display = ['name', 'code','status']
#     list_filter = ['status']


# class SettingLangAdmin(admin.ModelAdmin):
#     list_display = ['title', 'keywords','description','lang']
#     list_filter = ['lang']

admin.site.register(Setting,SettingtAdmin)
admin.site.register(SliderImage,SliderImageAdmin)
# admin.site.register(SettingLang,SettingLangAdmin)
# admin.site.register(ContactMessage,ContactMessageAdmin)
# admin.site.register(FAQ,FAQAdmin)
admin.site.register(showroom,showroomAdmin)
# admin.site.register(Language,LanguagesAdmin)


