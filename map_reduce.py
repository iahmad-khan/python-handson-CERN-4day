#!/usr/bin/python
from operator import add
data=open('input','r')
for line in data:
 sum=reduce(add,map(int,line.split()))
 print sum
