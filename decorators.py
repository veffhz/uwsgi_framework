from functools import wraps
import logging

from response import Response
from request import RequestGet

handlers = {}


def get(url):
    def decorator(app):
        @wraps(app)
        def wrapper(environ, start_response):
            headers = [('Content-Type', 'text/html')]
            data = app(RequestGet(environ))
            return Response(headers, start_response, "200 OK", data)

        handlers[url] = wrapper
        logging.info('path {} to get request mapped.'.format(url))
        return wrapper
    return decorator


def post(url):
    def decorator(app):
        @wraps(app)
        def wrapper(environ, start_response):
            start_response("200 OK", [('Content-Type', 'text/html')])
            return app(environ)

        handlers[url] = app
        logging.info('path {} to post request mapped.'.format(url))
        return wrapper
    return decorator
