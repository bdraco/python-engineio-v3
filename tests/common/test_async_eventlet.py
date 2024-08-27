import logging
import unittest

import six

if six.PY3:
    from unittest import mock
else:
    import mock

from engineio_v3.async_drivers import eventlet as async_eventlet
import pytest


class TestAsyncEventlet(unittest.TestCase):
    def setUp(self):
        logging.getLogger('engineio_v3').setLevel(logging.NOTSET)

    def test_bad_environ(self):
        wsgi = async_eventlet.WebSocketWSGI(None)
        environ = {'foo': 'bar'}
        start_response = 'bar'
        with pytest.raises(RuntimeError):
            wsgi(environ, start_response)

    @mock.patch(
        'engineio_v3.async_drivers.eventlet._WebSocketWSGI.__call__',
        return_value='data',
    )
    def test_wsgi_call(self, _WebSocketWSGI):
        _WebSocketWSGI.__call__ = lambda e, s: 'data'
        environ = {'eventlet.input': mock.MagicMock()}
        start_response = 'bar'
        wsgi = async_eventlet.WebSocketWSGI(None)
        assert wsgi(environ, start_response) == 'data'
