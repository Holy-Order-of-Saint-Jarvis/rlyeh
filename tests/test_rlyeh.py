# coding: utf-8

"""
Test the top-level module.
"""

import rlyeh


def test_version():
    # there is a __version__ attribute
    assert hasattr(rlyeh, '__version__')

    # __version__ can be compared to '18.4.0'
    assert rlyeh.__version__ >= '18.4.0'
