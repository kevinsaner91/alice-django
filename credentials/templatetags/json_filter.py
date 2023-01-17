from django import template
import json

register = template.Library()

@register.filter
def is_json(json_data):
    try:
        json.loads(json_data)
    except ValueError as e:
        return False
    return True
