"""Rest Server tests."""

# pylint:disable=attribute-defined-outside-init
import os.path
import sys
import shutil
import tempfile
from unittest import mock

import webtest

from rapstorebuilder import log
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


class TestMain():
    """Test main function."""
    def setup_method(self):
        """Tests per method setup."""
        self.bottle_run = mock.patch('bottle.run').start()
        self.tmpdir = self._create_tmpdir()

    @staticmethod
    def _create_tmpdir():
        """Create a temp directory for test.

        Use 'TMPDIR' provided by tox as base if available.
        """
        tmpdir = os.environ.get('TMPDIR', '.')
        tmpdir = tempfile.mkdtemp(dir=tmpdir)
        return tmpdir

    def teardown_method(self):
        """Cleanup tests mock."""
        mock.patch.stopall()
        shutil.rmtree(self.tmpdir)

    def test_main(self):
        """Test main function."""
        argv = ['rest_server.py', 'localhost', '8080']
        with mock.patch.object(sys, 'argv', argv):
            rest_server.main()
        assert self.bottle_run.called

    def test_main_logdir(self):
        """Test main function with a logdir."""
        argv = ['rest_server.py', 'localhost', '8080', '--logdir', self.tmpdir]
        with mock.patch.object(sys, 'argv', argv):
            rest_server.main()
        assert os.path.isfile(os.path.join(self.tmpdir, log.DEBUGFILE))
        assert os.path.isfile(os.path.join(self.tmpdir, log.ERRORFILE))
