def on_tag(tag, data):
    return "<{}>{}</{}>".format(tag, data, tag).encode('utf-8')
