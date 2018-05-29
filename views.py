from urls import Request
request = Request()


@request.get(url="/")
def welcome(request):
     return [b'Welcome to WSGI application!']


@request.get(url="/admin")
def admin(request):
    return [b'Admin WSGI application']
