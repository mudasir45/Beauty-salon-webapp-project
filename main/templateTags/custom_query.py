from django import template
from django.template import Library
from main.models import *

register = Library()

@register.filter
def discounted_price(price, di):
    Service = services.objects.get(id = id)
    Images = serviceImages.objects.filter(service = Service)
    return str(Images)
