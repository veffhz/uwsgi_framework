
class Request:

    URLS = {}

    def get(self, url):
        def decorator(app):
            Request.URLS[url] = app
            print('path {} to get request mapped.'.format(url))
            return app

        return decorator

    def post(self, url):
        def decorator(app):
            Request.URLS[url] = app
            print('path {} to post request mapped.'.format(url))
            return app

        return decorator
