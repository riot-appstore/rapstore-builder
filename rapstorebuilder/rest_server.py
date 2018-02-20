"""RAPStore Builder and Storage REST server implementation."""

import logging
import argparse

import bottle

import rapstorebuilder.log


PARSER = argparse.ArgumentParser()
PARSER.add_argument('host', help='Server address to bind to')
PARSER.add_argument('port', type=int, help='Server port to bind to')
PARSER.add_argument('--logdir', help='Directory to save logs')

LOGGER = logging.getLogger(__name__)


class BuilderRESTServer(bottle.Bottle):
    """Builder and Storage REST server."""
    WSGI_SERVER = 'paste'

    def __init__(self):
        super().__init__()

        self._register_routes()

    def _register_routes(self):
        """Regiter REST server routes."""
        self.route('/hello', 'GET', self.hello)

    def run(self, **kwargs):
        """Run server with specific default options."""
        kwargs.setdefault('server', self.WSGI_SERVER)

        super().run(**kwargs)

    # Routes callbacks

    @staticmethod
    def hello():
        """Hello world test route."""
        LOGGER.info('hello')
        return 'Hello World!\n'


def main():
    """Start REST Server."""
    opts = PARSER.parse_args()

    rapstorebuilder.log.configure_logging(opts.logdir)

    server = BuilderRESTServer()
    server.run(host=opts.host, port=opts.port, quiet=True)
