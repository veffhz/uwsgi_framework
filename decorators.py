import logging

from functools import wraps
from http import HTTPStatus
from response import Response
from request import RequestGet

from response_helpers import is_tuple
from response_helpers import is_tuple_with_headers
from response_helpers import get_code_name

handlers = {}


def get(url):
    def decorator(app):
        @wraps(app)
        def wrapper(environ, start_response):
            default_headers = [('Content-Type', 'text/html')]
            handler_result = app(RequestGet(environ))
            handler_headers = {}
            status_code = HTTPStatus.OK

            if is_tuple_with_headers(handler_result):
                response_text, status_code, handler_headers = handler_result
            elif is_tuple(handler_result):
                response_text, status_code = handler_result
            else:
                response_text = handler_result

            status = get_code_name(status_code)
            headers = dict(default_headers)
            headers.update(dict(handler_headers))
            print(headers)
            return Response(list(headers.items()), start_response, status, response_text)

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
