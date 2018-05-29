import logging

from urls import urls_handlers
import template


def apply_decorators():
    from views import admin
    from views import welcome


class Application:

    def __init__(self, _urls):
        self.urls = _urls

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        if path in self.urls:
            self.app = self.urls[path](environ, start_response)
        else:
            return self.not_found_handler(start_response)

        try:
            return self.app
        except Exception as e:
            logging.warning(e)
            return self.error_handler(start_response)

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


apply_decorators()


application = Application(urls_handlers)
