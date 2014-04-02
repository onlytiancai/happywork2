import init
init.init()

from happywork2 import application
app = application.app


def test_index():
    response = app.request('/subapp/', method='GET')
    assert response.data == "Hello sub app."
