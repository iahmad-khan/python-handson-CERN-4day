#!/usr/bin/python
from __future__ import generators  # only in Python 2.2

def gen_ints(start, stop):
    while start < stop:
        yield start       # next(...)
        start += 1
    return                # StopIteration
