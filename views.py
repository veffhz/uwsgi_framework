import template
from decorators import get, handlers


def get_handlers():
    return handlers


@get(url="/")
def welcome(request):
    content = 'Welcome to WSGI application!'
    return [template.on_page(content)]


@get(url="/admin")
def admin(request):
    content = 'Admin WSGI application'
    return [template.on_page(content)]
