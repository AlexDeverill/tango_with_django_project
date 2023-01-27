from django.contrib import admin
from rango.models import *

class PageAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'url')

# Register your models here.
admin.site.register(Category)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)