# -*- coding: utf-8 -*-
import web
import json


class register(object):
    def POST(self):
        return json.dumps(dict(code=200, message='Ok'))

urls = ("/api/register", "register",
        )
app = web.application(urls, globals())
