import init
init.init()


import application

app = application.app


def test_index():
    response = app.request('/', method='GET')
    assert response.data == "Hello word."


def test_raise():
    response = app.request('/raise', method='GET')
    assert response.status == "500 Internal Server Error"


def test_admin_unauthorized():
    response = app.request('/admin', method='GET')
    assert response.status == "401 Unauthorized"


def test_login_and_admin():
    b = app.browser()
    response = b.open('/login/dnspod').read()
    assert response == "dnspod logined."

    response = b.open('/admin').read()
    assert response == "welcome dnspod."
