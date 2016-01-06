# -*- coding: utf-8 -*-
"""
R_IRISSeismic - Python Wrappers for the IRISSeismic R Package
===================================================
Capabilities include creation of IRISSeismic Trace and Stream objects
from ObsPy Trace and Stream objects.

:copyright:
    Mazama Science
:license:
    GNU Lesser General Public License, Version 3
    (http://www.gnu.org/copyleft/lesser.html)

"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import *  # NOQA

from .stream import R_createTraceHeader, R_createTrace, R_createStream

if __name__ == '__main__':
    import doctest
    doctest.testmod(exclude_empty=True)

