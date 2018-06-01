import re
from http.client import responses
from template import on_tag


def get_code_name(status_code):
    return '%s %s' % (
            status_code,
            responses.get(status_code, 'Default Code Message')
        )


def is_tuple(handler_result):
    return isinstance(handler_result, tuple) and len(handler_result) == 2


def is_tuple_with_headers(handler_result):
    return isinstance(handler_result, tuple) and len(handler_result) == 3


def not_allowed_handler(start_response):
    status = "405 Method Not Allowed"
    headers = [('Content-Type', 'text/html')]
    start_response(status, headers)
    yield on_tag("h3", status)


def compile_url(url):
    if url == '/':
        text = r'^/$'
    else:
        text = r'^{}'
    return re.compile(text.format(url))
