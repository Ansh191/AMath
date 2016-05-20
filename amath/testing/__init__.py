import sys

if sys.version_info[0] < 3:
    from .number import *
    from .types import *
else:
    from .num3 import *
