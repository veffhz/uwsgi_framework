class Response:
    def __init__(self, headers, start_response, status, response_text=''):
        self.headers = headers
        self.start_response = start_response
        self.status = status
        self.response_text = response_text

    def __iter__(self):
        self.start_response(self.status, self.headers)
        yield self.response_text
