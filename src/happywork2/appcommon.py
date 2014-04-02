# -*- coding: utf-8 -*-
'''
### 实现功能

- 应用日志记录到/var/log下，并且滚动更新
- 用修饰器自动捕捉方法的异常并记录日志
- 用修饰器确保某些操作需要用户登录
- 使用session
- 网站favicon.ico的处理
- 拦截网站所有500错误并记录日志，或者发送邮件给开发人员

'''
import os
import web
import logging
import logging.handlers

from happywork2 import settings

########## Initialization

# 以下两项需要init函数初始化
app = None
session = None


def init(init_app):
    global app, session
    app = init_app

    # INFO: 可以自定义session存储器
    session = web.session.Session(app, web.session.DiskStore('sessions'),
                                  initializer={'count': 0})
    app.internalerror = internalerror
    app.add_processor(web.loadhook(session_hook))


logger = logging.getLogger(settings.LOGGER_NAME)


def init_logger():
    '初始化日志记录器，默认每100M一个文件'
    logger.setLevel(settings.LOG_LEVEL)
    logger.propagate = False
    handler = logging.handlers.RotatingFileHandler(settings.LOG_FILENAME,
                                                   maxBytes=100 * 1000 * 1000,
                                                   backupCount=10)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

init_logger()


def log_exception(op_name=None, rethrow=True):
    '''自动记录异常信息的修饰器，op_name:操作名称，
    rethrow：捕获异常后是否重新抛出'''
    def inner(fun):
        def inner2(*args, **kargs):
            fun_name = op_name if op_name is not None else fun.__name__
            try:
                return fun(*args, **kargs)
            except:
                logger.exception("%s error:args=%s, kargs=%s",
                                 fun_name, args, kargs)
                if rethrow:
                    raise
        return inner2
    return inner


def ensure_login(fun):
    '确认该操作需要用户登录'
    def inner(*args, **kargs):
        # INFO: 具体判断是否登录的规则可以改
        if not session.get("username"):
            raise web.unauthorized()
        return fun(*args, **kargs)
    return inner


def internalerror():
    '拦截所有500错误，记录日志或发送邮件给开发人员'
    import traceback
    error_msg = traceback.format_exc()
    # INFO: 可以在发生500错误时给自己发邮件
    logger.error("internalerror:%s", error_msg)

    # INFO: 可以替换成一个默认500页
    return web.internalerror("500 error")


def session_hook():
    '让每个web action都能取到session'
    web.ctx.session = session

_base_dir = os.path.dirname(__file__)
_tpl_dir = os.path.join(_base_dir, 'templates')
base_render = web.template.render(_tpl_dir, base='layout')
