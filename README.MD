#### WSGI app implementation

```
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Hello world from a simple WSGI application!']
```

Challenge 3

Write custom wsgi implementation.

Get helloWorld-function as base. Add request parsing, routing, throwing request to view, generate answer, return answer.


##### Usage:

Put your code in views.py file and decorate function request method with url parameter.
Function takes Request object and return raw html content, or content and status, or content, status and custom headers.


```
uwsgi --http :9090 --wsgi-file wsgi.py
```
