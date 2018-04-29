================
:octopus: R'lyeh
================

.. image:: https://img.shields.io/travis/Holy-Order-of-Saint-Jarvis/rlyeh.svg?style=flat-square
   :alt: Travis
   :target: https://travis-ci.org/Holy-Order-of-Saint-Jarvis/rlyeh

.. image:: https://img.shields.io/codecov/c/github/Holy-Order-of-Saint-Jarvis/rlyeh.svg?style=flat-square
   :alt: Codecov
   :target: https://codecov.io/gh/Holy-Order-of-Saint-Jarvis/rlyeh

Tecthulu API and simplified Ingress game model.

Development
===========

All contributors should be familiar with the `Contributor Covenant <CONDUCT.rst>`_.

``rlyeh`` uses `setuptools`_ for build management,
`pipenv`_ for dependency management,
and `tox`_ for environment management.

.. _pipenv: https://pipenv.readthedocs.io/
.. _setuptools: https://setuptools.readthedocs.io/
.. _tox: https://tox.readthedocs.io/

To get the latest development version of ``rlyeh``::

  ~$ git clone https://github.com/Holy-Order-of-Saint-Jarvis/rlyeh

Once the repository has been checked out, you should initialize the `pipenv`_::

  ~$ cd rlyeh
  ~/rlyeh$ pipenv install

To run all code checks and test suites::

  ~/rlyeh$ tox

The **tox** command accepts a ``-e`` option to specify which test environments to run. To run only the unit tests::

  ~/rlyeh$ tox -e py36