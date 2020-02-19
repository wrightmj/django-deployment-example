from django import template

register = template.Library()

@register.filter(name='cut_mw')
def cut_mw(value, arg):
    """
    This cuts out all value of "arg" from string!
    """
    return value.replace(arg, '')

# @register.filter
# def cutout(value, arg):
#     return value.replace(arg, '')


