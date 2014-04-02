# -*- coding: utf-8 -*-
'''
服务启动入口
'''
import web

import appcommon
import app_test.application
import app_subapp.application

urls = ["/favicon.ico", app_test.application.favicon,
        "/", app_test.application.index,
        "/raise", app_test.application.raise_exception,
        "/login/([^/]+)", app_test.application.login,
        "/admin", app_test.application.admin,
        "/subapp", app_subapp.application.app,
        ]


app = web.application(urls, globals())
appcommon.init(app)
