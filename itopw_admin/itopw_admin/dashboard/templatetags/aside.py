from django import template

register = template.Library()


@register.filter(name='nav_active')
def nav_active(value, arg):
    """return active class"""
    if value == arg:
        return 'kt-menu__item--active'
    return ''
