"""Generic tests rapstorebuilder package."""


import pkg_resources

import rapstorebuilder


def test_version_string():
    """Test version string is valid.

    Parsed version should be the same as saved one.
    """
    version = rapstorebuilder.__version__
    parsed = pkg_resources.parse_version(version)
    assert version == str(parsed)
