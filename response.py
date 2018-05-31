class Response:
    def __init__(self, headers, start_response, code=200, data=''):
        self.headers = headers
        self.start_response = start_response
        self.code = code
        self.data = data

    def __call__(self):
        pass

    def __iter__(self):
        print(self.data)
        self.start_response(self.code, self.headers)
        yield self.data
