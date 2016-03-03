#!/usr/bin/python
from time import time as tik

#recursive fib
def fib(n):
  if n<2:
    return 1
  else:
    return fib(n-1) + fib(n-2)
#iterative fib
def fibi(n):
  current,previous=1,1
  while n>1:
    current,previous = current+previous , current
    n -=1
  return current


def time(f,*args,**kwds):
  t1=tik()
  result=f(*args,**kwds)
  t2=tik()
  return t2-t1,result

"""def memo(func):
  store={}
  def get_it(*args):
    try:
      return store[args]
    except KeyError: 
      return store.setdefault(args, func(*args))
  return get_it
"""
class memo:
  
  def __init__(self,func):
    self.store = {}
    self.func=func

  def __call__(self,*args):
    try:
      return self.store[args]
    except KeyError: 
      return self.store.setdefault(args, self.func(*args))
