# -*- coding: utf-8 -*-
import web

from happywork2 import appcommon


class favicon(object):
    'favicon.ico配置'
    def GET(self):
        # INFO: 具体图标可以在这里改
        return web.found("https://www.dnspod.cn/yantai/img/index/tqq.ico")


class index(object):
    '首页'
    def GET(self):
        client_ip = web.ctx.env.get('HTTP_X_REAL_IP', web.ctx.ip)
        appcommon.logger.debug("recv /index request: client_ip: %s", client_ip)
        return "Hello word."


class raise_exception(object):
    '测试一个500错误页'
    @appcommon.log_exception("raise action")
    def GET(self):
        raise Exception("opps")


class login(object):
    '登录页面'
    def GET(self, username):
        web.ctx.session.username = username
        return "%s logined." % username


class admin(object):
    '需要登录后才能访问'
    @appcommon.ensure_login
    def GET(self):
        return "welcome %s." % web.ctx.session.username
