import os

project = {{ cookiecutter.project | pprint }}
package = {{ cookiecutter.package | pprint }}
src = {{ cookiecutter.__src | pprint }}
nslevel = {{ cookiecutter.nslevel | int }}

{% set nstype = cookiecutter.nstype %}
{% if nstype == "pep420" %}
NAMESPACE_INIT = None
{% else %}
NAMESPACE_INIT = """\
'namespace package %s'
# see `PEP420 <https://peps.python.org/pep-0420/>`_
# https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#legacy-namespace-packages
# https://docs.python.org/3/library/pkgutil.html#pkgutil.extend_path
{% if nstype == "setuptools" -%}
__import__('pkg_resources').declare_namespace(__name__)
{% endif -%}
{% if nstype == "setuptools+pkgutil" -%}
try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
{% endif -%}
{% if nstype == "pkgutil" -%}
__path__ = __import__('pkgutil').extend_path(__path__, __name__)
{% endif -%}
"""
{% endif %}

# generate intermediate inits for a.b.c.package
parts = package.split('.')
for partno, part in enumerate(parts[:-1], 1):
    pkg = '.'.join(parts[:partno])
    path = os.path.join(project, src, *parts[:partno], '__init__.py')
    if nslevel == -1 or partno <= nslevel:
        content = None if NAMESPACE_INIT is None else NAMESPACE_INIT % pkg
    else:
        content = ''
    if content is not None:
        with open(path, 'w') as fp:
            fp.write(content)
