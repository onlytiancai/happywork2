# -*- coding: utf-8 -*-
from happywork2 import webmain

app = webmain.app
wsgiapp = app.wsgifunc()

if __name__ == '__main__':
    app.run()
