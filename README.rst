==========
systeminfo
==========


.. image:: https://img.shields.io/pypi/v/systeminfo.svg
        :target: https://pypi.python.org/pypi/systeminfo

.. image:: https://img.shields.io/travis/crotty-d /systeminfo.svg
        :target: https://travis-ci.org/crotty-d /systeminfo

.. image:: https://readthedocs.org/projects/systeminfo/badge/?version=latest
        :target: https://systeminfo.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Python package to get basic system information.


* Free software: MIT license
* Documentation: https://systeminfo.readthedocs.io.


Features
--------

* Provides basic information about the system on which it's run via the *platform* Python module.
* Provides the functions *get_platform_info()*, *get_machine_info()* and *get_version_info()* to access different kinds of system information.
* Running the *sysinfo.py* file or entering the *sysinfo* console command (after adding it to your Python path) prints the system information via the above functions
Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
