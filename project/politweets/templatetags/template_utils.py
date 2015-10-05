
from django import template
register = template.Library()

@register.filter(name='percentage')
def percentage(count, total):
    try:
        return "%.0f" % ((float(count) / float(total)) * 100)
    except ValueError:
        return ''

