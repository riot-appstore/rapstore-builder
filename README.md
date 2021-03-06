Builder and storage service
===========================


Service that handles building and storing/downloading RIOT repository.

It is implemented as a REST service using `bottle`.

Usage
-----

    usage: rapstore-builder [-h] [--logdir LOGDIR] host port

    positional arguments:
    host             Server address to bind to
    port             Server port to bind to

    optional arguments:
    -h, --help       show this help message and exit
    --logdir LOGDIR  Directory to save logs


Documentation
-------------

The generated documentation is stored in `docs` and should be kept updated in
the master branch.

It can be generated with

    tox -e doc

Last master version its also available on:

    https://riot-appstore.github.io/rapstore-builder/


Design
------

https://github.com/riot-appstore/internal/wiki/Builder-repository-storage-service


Testing
-------

Testing is done by running `tox`:

    $ tox
    ...
      py35-pylint: commands succeeded
      py35-flake8: commands succeeded
      py35-tests: commands succeeded
      py35-checksetup: commands succeeded
      doc: commands succeeded
      congratulations :)


Install `tox` from your package manager or with pip.

    sudo apt install tox

or

    pip3 install tox


All tests dependencies will be downloaded by `tox` itself.


### Testing without tox

If you want to run tests without tox, install the tests dependencies with:

    pip3 install -r tests_utils/test-requirements.txt

And then run the commands described in `tox.ini`.
