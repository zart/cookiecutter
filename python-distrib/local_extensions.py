'custom jinja2 filters for cookiecutter'
import re
from cookiecutter.utils import simple_filter


@simple_filter
def slug(x, separator='.'):
    'Convert phrases or camelcased strings to separated lower cased strings'
    # first we split on spaces
    parts = x.split()
    # if that doesnt work, split on camel case
    if len(parts) == 1:
        parts = re.split(r'(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])', x)
    # lowercase everything and join via separator
    out = separator.join(part.lower() for part in parts)
    return out
