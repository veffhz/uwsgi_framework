from http.client import responses


def get_code_name(status_code):
    return '%s %s' % (
            status_code,
            responses.get(status_code, 'Default Code Message')
        )


def is_tuple(handler_result):
    return isinstance(handler_result, tuple) and len(handler_result) == 2


def is_tuple_with_headers(handler_result):
    return isinstance(handler_result, tuple) and len(handler_result) == 3