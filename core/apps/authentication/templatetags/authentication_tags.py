from django import template

register = template.Library()


@register.filter(name="has_group")
def has_group(user, group):
    return user.groups.filter(name=group).exists()
