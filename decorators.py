def get(url):
    def decorator(app):
        from wsgilib.routes import Request
        Request.URLS[url] = app
        print('path {} to get request mapped.'.format(url))
        return app
    return decorator


def post(url):
    def decorator(app):
        from wsgilib.routes import Request
        Request.URLS[url] = app
        print('path {} to post request mapped.'.format(url))
        return app
    return decorator
