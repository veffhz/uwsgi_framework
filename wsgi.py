from urls import Request


def apply_decorators():
    from views import admin
    from views import welcome


class Application:

    def __init__(self, _urls):
        self.urls = _urls

    def __call__(self, environ, start_response):
        uri = environ['PATH_INFO']

        if uri not in self.urls:
            self.app = self.not_found_handler
        else:
            self.app = self.urls[uri]

        try:
            result = self.app(environ, start_response)
            for item in result:
                yield item
        except Exception as e:
            print(e)
            return self.error_handler(environ, start_response)

    @staticmethod
    def not_found_handler(environ, start_response):
        status = "404 Not Found"
        headers = [('Content-Type', 'text/html')]
        start_response(status, headers)
        return [b"HTTP 404"]

    @staticmethod
    def error_handler(environ, start_response):
        status = "500 Internal Server Error"
        headers = [('Content-Type', 'text/html')]
        start_response(status, headers)
        return [b"Internal Server Error 500"]


apply_decorators()


application = Application(Request.URLS)
