# -*- coding: utf-8 -*-
import web


def init():
    import sys
    sys.path.append('../src')

    def debugwrite(x):
        pass
    web.debug.write = debugwrite  # 关掉调试日志
