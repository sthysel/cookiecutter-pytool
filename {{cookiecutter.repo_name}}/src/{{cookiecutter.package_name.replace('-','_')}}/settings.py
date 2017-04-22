import os
from xdg.BaseDirectory import xdg_cache_home

__version__ = '0.1.0'

NAME={{cookiecutter.package_name}}
CACHE = os.getenv('PIBAKE_CACHE', os.path.join(xdg_cache_home, NAME))
