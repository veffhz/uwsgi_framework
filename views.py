from wsgilib.routes import Request
request = Request()


@request.get(url="/")
def welcome(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Welcome to WSGI application!']


@request.get(url="/admin")
def admin(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Admin WSGI application']
