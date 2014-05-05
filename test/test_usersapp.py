# -*- coding: utf-8 -*-
import init
init.init()

import web
import json

import usersapp

app = usersapp.app


def expect_result_code(result, code):
    result = json.loads(result)
    assert result['code'] == code


def test_register():
    '''200 is ok
    400 is error
    '''

    # 第一次能注册成功
    req_data = web.storage(username='wawa', password='123456')
    response = app.request('/api/register', method='POST', data=req_data)
    expect_result_code(response.data, 200)
