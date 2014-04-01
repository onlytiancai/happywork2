# -*- coding: utf-8 -*-
"""
保存配置信息，开发环境，测试环境，生产环境可使用不同配置
然后生产环境的配置也用git来管理变更

"""
import web

env = "testing"

if env == "production":
    web.config.debug = False

    LOG_FILENAME = '/var/log/webpy_bootstrip.log'
    LOG_LEVEL = "INFO"
    LOGGER_NAME = "webpy_bootstrip"

elif env == "testing":
    web.config.debug = True

    LOG_FILENAME = '/var/log/webpy_bootstrip.log'
    LOG_LEVEL = "DEBUG"
    LOGGER_NAME = "webpy_bootstrip"
