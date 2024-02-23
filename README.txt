Cookiecutter
============


Collection of templates for creating various Python projects using
cookiecutter_ tool. The provided templates are opionated and hardcode some
assumptions. YMMV. Templates are open-sourced under MIT license.

.. _cookiecutter: https://cookiecutter.readthedocs.io/

How to use
----------

Install cookiecutter itself first::

    $ pip install cookiecutter

Then invoke it like so::

    $ cookiecutter gh:zart/cookiecutter
    $ cookiecutter gh:zart/cookiecutter project="My python app" package="myapp"


Provided templates
------------------

Not all templates support features beyond bare necceseties. There is also no
checking of validity whatsoever, so generated templates might be unusable.

All templates use `_output_dir`` as a root, which defaults to current directory
in cookiecutter unless overridden by -o option in cli.

Parameter `project` is assumed to be unmangled project name and project
directory should be slugified version of that.


empty
~~~~~

Simplest template there is without any parameters. Mostly for demo purposes.


python-module
~~~~~~~~~~~~~

Uses `project` and `module` parameters to generate project with module inside.
Uses fixed src-layout and does not support namespace packages. Mostly for demo
purposes as well.


python-package
~~~~~~~~~~~~~~

Generates python package with a simple readme and no packaging.
Adds namespace package support upon `python-module` template.

Uses `project` and `package` parameters. `package` name may be dotted and
parent packages will be generated automatically depending on `nslevel` and
`nstype` parameters.

`__src` defaults to 'src' and puts package in there for src-layout style.
Can be overridden as empty string for using flat-style.

`nslevel` is an integer that specifies how many levels from top should be
generated as namespace packages. -1 means every package above, 0 means none,
etc.

`nstype` chooses how to generate namespace package:

pep420
  `PEP 420 <https://peps.python.org/pep-0420/>`_ uses empty directories and
  is explicitly exclusive with other options

pkgutil
  uses `pkgutil.extend_path`_ API from stdlib

setuptools
  uses setuptools' `pkg_resources.declare_namespace`_ API from setuptools

setuptools+pkgutil
  combines both methods with pkgutil being fallback


Choice of type depends on target python version.
Modern code should favour PEP420-style namespace packages for their simplicity.
This requires at least Python 3.3 and is not supported by any 2.* version.

Setuptools option requires explicit support from packaging and might be used for
compatibility with existing code. Supports namespace packages in zip archives.

Pkgutil provides basic namespace support from stdlib, does not support zip
archives but adds special handling of .pkg files akin to .pth ones.

.. _`pkgutil.extend_path`: https://docs.python.org/3/library/pkgutil.html#pkgutil.extend_path
.. _`pkg_resources.declare_namespace`: https://setuptools.pypa.io/en/latest/pkg_resources.html#namespace-package-support


python-distrib
~~~~~~~~~~~~~~

Builds upon `python-package` template, uses all its options and adds python
packaging.
Setuptools>=61 are hardcoded for now which means python should be at least 3.7.

Added following parameters to generate package metadata:

`project`
  same as templates above uses full project name. Slugified version is used for
  directory and package name.

`package`
  same as templates above, sets full dotted name to python package

`version`
  distribution version. Hardcoded as static property.
  Dynamic version support requires changes to pyproject.toml

`description`
  short package description.
  NOTE: Long description will be concatenation of readme and changelog files.

`license`
  package licensing.
  TODO: MIT is hardcoded for now

`author` and `author_email`
  principal package author contact
