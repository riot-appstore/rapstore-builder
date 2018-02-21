"""RAPStore Builder and Storage REST server implementation."""

import logging
import argparse
import base64

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
        self.route('/builder/build/riot_application/<riot_uuid>/<board>',
                   'POST', self.build_application)

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

    def build_application(self, riot_uuid, board):
        # pylint:disable=line-too-long
        # flake8: noqa
        """Build requested application.

        :param riot_uuid: RIOT version UUID
        :param board: RIOT internal board name

        :<json string application_directory: application relative path in RIOT

        :>json int build_ret: Build return value
        :>json string build_out: Build output
        :>json JSONObject files: map of files by extension
          ``"ext": base64(content.ext)``

        **Example request**:

        .. sourcecode:: http

          POST /builder/build/riot_application/a8098c1a-f86e-11da-bd1a-00112444be1e/iotlab-m3 HTTP/1.1
          Content-Type: application/json

          {
              "application_directory": "examples/default"
          }

        **Example response**:

        .. sourcecode:: http

          HTTP/1.1 200 OK
          Content-Type: application/json

          {
              "build_out": "Building application\\nOK\\n",
              "build_ret": 0,
              "files": {
                  "elf": "f0VMRg=="
              }
          }
        """
        # flake8: qa
        # pylint:enable=line-too-long

        assert riot_uuid
        assert board

        # DUMMY version that returns a fake elf file
        buildout = self._build()
        for name, binfile in buildout['files'].items():
            buildout['files'][name] = self._to_base64(binfile)

        return buildout

    @staticmethod
    def _build():
        out = {
            'files': {
                'elf': b'\x7fELF',
            }
        }
        out['build_ret'] = 0
        out['build_out'] = 'Building application\nOK\n'
        return out

    @staticmethod
    def _to_base64(binfile):
        """Encode buildout to be sendable as JSON."""
        return base64.b64encode(binfile).decode('ascii')


def main():
    """Start REST Server."""
    opts = PARSER.parse_args()

    rapstorebuilder.log.configure_logging(opts.logdir)

    server = BuilderRESTServer()
    server.run(host=opts.host, port=opts.port, quiet=True)
