from wsgilib.urls import Request


def not_found(environ, start_response):
    status = "404 Not Found"
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    return [b"HTTP 404"]


def internal_error(environ, start_response):
    status = "500 Internal Server Error"
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    return [b"Internal Server Error 500"]


class Routing:

    def __init__(self, _urls):
        self.urls = _urls

    def __call__(self, environ, start_response):
        uri = environ['REQUEST_URI']

        if uri not in self.urls:
            self.app = not_found
        else:
            self.app = self.urls[uri]

        try:
            result = self.app(environ, start_response)
            for item in result:
                yield item
        except Exception as e:
            print(e)
            return internal_error(environ, start_response)


application = Routing(Request.URLS)
