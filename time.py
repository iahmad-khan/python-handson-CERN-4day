#!/usr/bin/python
from time import time as tik
def time(f,*args,**kwds):
  t1=tik()
  result=f(*args,**kwds)
  t2=tik()
  return t2-t1,result
  

