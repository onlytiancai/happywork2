# -*- coding: utf-8 -*-
'''
服务启动入口
'''
import web

from common import bootstrap
import controllers.default

urls = ["/favicon.ico", controllers.default.favicon,
        "/", controllers.default.index,
        "/raise", controllers.default.raise_exception,
        "/login/([^/]+)", controllers.default.login,
        "/admin", controllers.default.admin,
        ]


app = web.application(urls, globals())
bootstrap.init(app)
