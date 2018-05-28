####WSGI app implementation

```
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Hello world from a simple WSGI application!']
```

Challenge 3

Написать свой wsgi веб-фреймворк.

За основу взять пример выше. Добавить парсинг запроса, обработку роутинга, проброс запроса во view, генерацию ответа, проброс её наружу..

```
uwsgi --http :9090 --wsgi-file wsgi_impl.py
```


{'REQUEST_METHOD': 'GET', 'REQUEST_URI': '/run', 'PATH_INFO': '/run', 'QUERY_STRING': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 'SCRIPT_NAME': '', 'SERVER_NAME': 'thinkPad', 'SERVER_PORT': '9090', 'UWSGI_ROUTER': 'http', 'REMOTE_ADDR': '127.0.0.1', 'REMOTE_PORT': '63653', 'HTTP_HOST': 'localhost:9090', 'HTTP_USER_AGENT': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0', 'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'HTTP_ACCEPT_LANGUAGE': 'en-GB,en;q=0.5', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate', 'HTTP_CONNECTION': 'keep-alive', 'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 'HTTP_CACHE_CONTROL': 'max-age=0', 'wsgi.input': <uwsgi._Input object at 0x7f12ad886798>, 'wsgi.file_wrapper': <built-in function uwsgi_sendfile>, 'wsgi.version': (1, 0), 'wsgi.errors': <_io.TextIOWrapper name=2 mode='w' encoding='UTF-8'>, 'wsgi.run_once': False, 'wsgi.multithread': False, 'wsgi.multiprocess': False, 'wsgi.url_scheme': 'http', 'uwsgi.version': b'2.0.17', 'uwsgi.node': b'thinkPad'}
