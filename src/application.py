# -*- coding: utf-8 -*-
'''
服务启动入口
'''
import web

import appcommon
import testapp
import subapp

urls = ["/favicon.ico", testapp.favicon,
        "/", testapp.index,
        "/raise", testapp.raise_exception,
        "/login/([^/]+)", testapp.login,
        "/admin", testapp.admin,
        "/subapp", subapp.app,
        ]


app = web.application(urls, globals())
appcommon.init(app)
wsgiapp = app.wsgifunc()
if __name__ == '__main__':
    app.run()
