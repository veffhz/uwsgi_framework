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
uwsgi --http :9090 --wsgi-file wsgi.py
```
