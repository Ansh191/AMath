from __future__ import division, print_function

"""
AMath
=====


"""

from .Errors import *
from .DataTypes import *
from .Computation import *
from .lists import *
from .string_proccessing import *
from .testing import *
from .constants import *

# from .random import *
import sys

if sys.version_info[0] < 3:
    from .Errors.internet2 import test
    test()
    del test
else:
    from .Errors.internet3 import test
    test()
    del test

__all__ = list(n for n in dir() if n[:1] != '_')
