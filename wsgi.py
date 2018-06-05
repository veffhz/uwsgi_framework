"""
WSGI entry point
It exposes the WSGI callable as a module-level variable named ``application``.

"""


import logging
import template

from views import get_handlers


class Application:

    def __init__(self):
        self.handlers = get_handlers()

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO')
        app = self.find_handler(path)
        if app:
            self.app = app(environ, start_response)
        elif not path.endswith('/'):
            query_string = environ.get('QUERY_STRING')
            return self.trailing_slash_handler(path, query_string, start_response)
        else:
            return self.not_found_handler(start_response)

        try:
            return self.app
        except Exception as e:
            logging.warning(e)
            return self.error_handler(start_response)

    def find_handler(self, path):
        funcs = [self.handlers[x] for x in self.handlers.keys() if x.match(path)]
        return funcs[0]

    @staticmethod
    def not_found_handler(start_response):
        status = "404 Not Found"
        headers = [('Content-Type', 'text/html')]
        start_response(status, headers)
        yield template.on_tag("h3", status)

    @staticmethod
    def error_handler(start_response):
        status = "500 Internal Server Error"
        headers = [('Content-Type', 'text/html')]
        start_response(status, headers)
        yield template.on_tag("h3", status)

    @staticmethod
    def trailing_slash_handler(path, query_string, start_response):
        status = "301 Moved Permanently"
        if len(query_string) > 0:
            path = "%s/?%s" % (path, query_string)
        else:
            path = "%s/" % path
        headers = [('Location', '{}'.format(path))]
        start_response(status, headers)
        yield b''


application = Application()
