from django import template

register = template.Library()

@register.filter
def calculate_total_cloths(user):
    return user.topwear + user.bottomwear + user.woolenwear + user.otherclothes
