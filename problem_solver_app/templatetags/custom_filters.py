# problem_solver_app/templatetags/custom_filters.py (Optional, for splitlines)
# Create this file if you want to use the 'splitlines' filter.
# If you don't want to create this, you'll need to manually replace
# `solution_path|splitlines` with `solution_path.split('\n')` in the HTML.

from django import template

register = template.Library()

@register.filter
def splitlines(value):
    """Splits a string by newlines and returns a list of lines."""
    return value.split('\n')