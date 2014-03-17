from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def replaceUWS(sarg):
    return sarg.replace('_',' ')

