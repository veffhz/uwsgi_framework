from functools import wraps


class Request:

    URLS = {}

    def get(self, url):
        def decorator(app):

            @wraps(app)
            def wrapper(*args, **kwargs):
                return app()

            Request.URLS[url] = wrapper
            print('path {} to get request mapped.'.format(url))
            return wrapper
        return decorator

    def post(self, url):
        def decorator(app):

            @wraps(app)
            def wrapper(*args, **kwargs):
                return app()

            Request.URLS[url] = app
            print('path {} to post request mapped.'.format(url))
            return wrapper

        return decorator

