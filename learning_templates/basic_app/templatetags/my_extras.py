from django import template

register = template.Library()
@refister.filter(name='cutme')
def cut(value,arg):
    # This cuts out all values of arg from the string
    return value.replace(arg, "")

# register.filter('cutme',cut)
