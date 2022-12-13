from django import template
register = template.Library()


@register.filter
def index(query_set, x):
    return query_set[x]
