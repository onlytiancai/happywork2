# -*- coding: utf-8 -*-
import web

from happywork2 import appcommon
render = appcommon.base_render.subapp


class index(object):
    def GET(self):
        return "Hello sub app."


class tpl(object):
    def GET(self):
        return render.hello()

urls = ("/", "index",
        "/tpl", "tpl")
app = web.application(urls, globals())
