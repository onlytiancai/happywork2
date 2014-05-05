# -*- coding: utf-8 -*-
import init
init.init()

import web
from nose.tools import assert_raises


import appcommon


def test_Validator():
    data = web.storage()
    validator = appcommon.Validator(data)
    validator.addrule(name='username', required=True)
    assert_raises(appcommon.ValidationError, validator.check)

    data = web.storage(username='a')
    validator = appcommon.Validator(data)
    validator.addrule(name='username', minlen=3, maxlen=5)
    assert_raises(appcommon.ValidationError, validator.check)
    data.username = '12345678'
    assert_raises(appcommon.ValidationError, validator.check)
