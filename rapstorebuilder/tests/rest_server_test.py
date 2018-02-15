"""Rest Server tests."""

# pylint:disable=attribute-defined-outside-init
import sys
from unittest import mock

import webtest

from rapstorebuilder import rest_server


class TestBuilderRESTServer():
    """Test BuilderRESTServer class."""

    def setup_method(self):
        """Tests per method setup."""
        self.server = rest_server.BuilderRESTServer()
        self.app = webtest.TestApp(self.server)

    def test_hello(self):
        """Test '/hello' route."""
        ret = self.app.get('/hello')
        assert ret.text == 'Hello World!\n'


@mock.patch('bottle.run')
def test_main(bottle_run_mock):
    """Test main function"""
    argv = ['rest_server.py', 'localhost', '8080']
    with mock.patch.object(sys, 'argv', argv):
        rest_server.main()
    assert bottle_run_mock.called
