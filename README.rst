================
:octopus: R'lyeh
================

.. |license-badge| image:: https://img.shields.io/github/license/Holy-Order-of-Saint-Jarvis/rlyeh.svg?style=for-the-badge
   :alt: MIT-licensed software (link to license in source control)
   :target: https://github.com/Holy-Order-of-Saint-Jarvis/rlyeh/blob/master/LICENSE

.. |travis-badge| image:: https://img.shields.io/travis/Holy-Order-of-Saint-Jarvis/rlyeh.svg?style=for-the-badge&logo=travis&label=CI
   :alt: current Continuous Integration build status (link to CI build)
   :target: https://travis-ci.org/Holy-Order-of-Saint-Jarvis/rlyeh

.. |codecov-badge| image:: https://img.shields.io/codecov/c/github/Holy-Order-of-Saint-Jarvis/rlyeh.svg?style=for-the-badge
   :alt: current code coverage status (link to code coverage)
   :target: https://codecov.io/gh/Holy-Order-of-Saint-Jarvis/rlyeh
   
|license-badge| |travis-badge| |codecov-badge|

Tecthulu API and simplified Ingress game model.

This package is a Python library only; it is used by the |toplevel|_ and |tecthulu-simulator|_ packages.

.. |toplevel| replace:: ``[name TBD]``
.. _toplevel: https://github.com/Holy-Order-of-Saint-Jarvis/toplevel/
.. |tecthulu-simulator| replace:: ``tecthulu-simulator``
.. _tecthulu-simulator: https://github.com/Holy-Order-of-Saint-Jarvis/tecthulu-simulator/

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
