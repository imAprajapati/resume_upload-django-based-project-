from atexit import register
from django import template
register=template.Library()
@register.filter(name='remove_spcial')
def remove_chars(value,arg):
    for character in arg:
        value=value.replace(character,'')
    return value