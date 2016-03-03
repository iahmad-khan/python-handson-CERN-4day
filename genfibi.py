#!/usr/bin/python
#from __future__  import generators
def fibi_gen():
  current,previous=1,1
  while True:
    current,previous = current+previous , current
    yield current

