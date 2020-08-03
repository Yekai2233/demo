# -*- coding: utf-8 -*-
from werkzeug.routing import BaseConverter


class Router:
    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        def decorator(f):
            self.mound.append((f, rule, options))
            return f

        return decorator

    def register(self, bp, url_prefix=None):
        if url_prefix is None:
            url_prefix = '/' + self.name
        for f, rule, options in self.mound:
            endpoint = self.name + '+' + \
                       options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *args):
        super(RegexConverter, self).__init__(url_map)
        self.url = url_map
        self.regex = args[0]   # 正则的匹配规则

    def to_python(self, value):
        return value
