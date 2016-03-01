#!/usr/bin/python
import sys
from functools import partial

f = open('/etc/passwd','r')

users_and_ids = []

for line in f:
  u,_,id,_ = line.split(':',3)
  users_and_ids.append((u,int(id)))


def make_key(n,pair):
  return pair[n]

users_and_ids.sort(key = partial(make_key,1))
for id,usr in users_and_ids:
  print id,usr


