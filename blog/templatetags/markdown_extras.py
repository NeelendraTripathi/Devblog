# blog/templatetags/markdown_extras.py

# Import Django's template library, which is where the tools for creating tags and filters live.
from django import template
# Import the markdown library we installed with pip.
import markdown as md

# Create an instance of the template library. This is the registry where we will
# add our new custom filter.
register = template.Library()

# This is a "decorator". It's a special tag that tells Django that the
# function directly below it is a template filter.
@register.filter()
def markdownify(text):
    # This is the core of our filter. It takes the text from the template,
    # runs it through the markdown library's main function, and returns the result.
    # 'fenced_code' is an extension for handling code blocks nicely.
    return md.markdown(text, extensions=['fenced_code'])
