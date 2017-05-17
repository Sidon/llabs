import os
import json
from django.core.exceptions import ImproperlyConfigured

fconf = os.path.dirname(os.path.abspath(__file__))
fconf = os.path.join(fconf, 'llabs.json')


# Comment for local.
fconf = '/etc/llabs.json'


def _get_config(setting):
    with open(fconf) as f:
        config = json.loads(f.read())

    try:
        return config[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {0} environment variable".format(setting))
