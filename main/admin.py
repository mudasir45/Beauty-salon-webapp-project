from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(category)
admin.site.register(order)
admin.site.register(profile)

class ServiceImageAdmin(admin.StackedInline):
    model = serviceImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ServiceImageAdmin]

admin.site.register(services, ProductAdmin)