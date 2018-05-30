from functools import wraps
import logging

urls_handlers = {}


def get(url):
    def decorator(app):
        @wraps(app)
        def wrapper(environ, start_response):
            start_response("200 OK", [('Content-Type', 'text/html')])
            return app(environ)

        urls_handlers[url] = wrapper
        logging.info('path {} to get request mapped.'.format(url))
        return wrapper

    return decorator


def post(url):
    def decorator(app):
        @wraps(app)
        def wrapper(environ, start_response):
            start_response("200 OK", [('Content-Type', 'text/html')])
            return app(environ)

        urls_handlers[url] = app
        logging.info('path {} to post request mapped.'.format(url))
        return wrapper

    return decorator
