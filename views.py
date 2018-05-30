import template
from decorators import get


def init():
    pass


@get(url="/")
def welcome(request):
    return [template.on_page('Welcome to WSGI application!')]


@get(url="/admin")
def admin(request):
    return [template.on_page('Admin WSGI application')]
