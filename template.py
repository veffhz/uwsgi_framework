def on_tag(tag, data):
    return "<{}>{}</{}>".format(tag, data, tag).encode('utf-8')


def on_page(data):
    return "<html><body>{}</body></html>".format(data).encode('utf-8')
