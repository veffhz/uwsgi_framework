from wsgilib.urls import Request
request = Request()


@request.get(url="/")
def welcome():
    #start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Welcome to WSGI application!']


@request.get(url="/admin")
def admin():
    #start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Admin WSGI application']
