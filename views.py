"""
Put your code in this file and decorate function
request method with url parameter.
Function takes Request object and return raw html
content, or content and status, or content, status
and custom headers.

"""


import template
from decorators import get, handlers


def get_handlers():
    return handlers


@get(url="/")
def welcome(request):
    content = 'Welcome to WSGI application!'
    return template.on_page(content), 200


@get(url="/admin/")
def admin(request):
    content = 'Admin WSGI application'
    return template.on_page(content)


@get(url="/debug/")
def debug(request):
    content = request
    return template.on_page(content), 200, [
        ('Custom-header-mode', 'DebugMode')
    ]
