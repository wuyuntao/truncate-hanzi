# -*- coding: UTF-8 -*-
from django.template import Library
from django.template.defaultfilters import stringfilter

register = Library()

@stringfilter
def truncatehanzi(value, arg):
    """
    Truncates a string after a certain number of words including
    alphanumeric and CJK characters.

    Argument: Number of words to truncate after.
    """
    from truncate_hanzi import truncate_hanzi
    try:
        length = int(arg)
    except ValueError: # Invalid literal for int().
        return value # Fail silently.
    return truncate_hanzi(value, length)
truncatehanzi.is_safe = True

register.filter('truncatehanzi', truncatehanzi)
