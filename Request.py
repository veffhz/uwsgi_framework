class RequestBase:
    def __init__(self, environ):
        self.environ = environ
        self.headers = self.parse_headers()

    def parse_headers(self):
        headers = {}
        length = self.environ.get('CONTENT_LENGTH', 0)
        headers['CONTENT_LENGTH'] = 0 if not length else int(length)

        headers_names = ['REQUEST_METHOD', 'PATH_INFO',
                         'REMOTE_ADDR', 'REMOTE_HOST',
                         'CONTENT_TYPE']

        for name in self.environ.keys():
            if name in headers_names:
                headers[name] = self.environ[name]
            elif 'HTTP' in name:
                headers[name] = self.environ[name]
        return headers


class RequestGet(RequestBase):
    def __init__(self, environ):
        super().__init__(environ)
        self.query_string = self.parse_query_string()

    def parse_query_string(self):
        params = {}
        query_string = self.environ.get('QUERY_STRING')
        if len(query_string) > 0:
            for param in query_string.split('&'):
                key, value = param.split('=')
                params[key] = str.replace(value, "/", '')
        return params

    def __str__(self):
        text = "{}:{} <br />"
        headers = [text.format(item, self.headers[item])
                   for item in self.headers.keys()]

        params = [text.format(item, self.query_string[item])
                  for item in self.query_string.keys()]
        return "<p>%s</p><p>%s</p>" % (str(headers), str(params))


class RequestPost:
    """TODO"""
    def __init__(self, data, start_response):
        pass
