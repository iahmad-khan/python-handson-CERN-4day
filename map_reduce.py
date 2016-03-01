#!/usr/bin/python
from operator import add

def my_int(token):
  try:
    return int(token)
  except ValueError:
    return 0
data=open('input','r')
for line in data:
  sum=reduce(add,map(my_int,line.split()),0)
  print sum
