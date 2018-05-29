import template
from urls import HttpRequest

request = HttpRequest()


@request.get(url="/")
def welcome(request):
    return [template.on_page('Welcome to WSGI application!')]


@request.get(url="/admin")
def admin(request):
    return [template.on_page('Admin WSGI application')]
