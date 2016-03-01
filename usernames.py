#!/usr/bin/python
import sys
def my_cmp(a, b):
  return cmp(a[1], b[1])


f = open('/etc/passwd','r')

users_and_ids = []

for line in f:
  u,_,id,_ = line.split(':',3)
  users_and_ids.append((u,int(id)))
#using cmp
#users_and_ids.sort(cmp=my_cmp)
#using lambda
users_and_ids.sort(key=lambda k:k[1])
for id,usr in users_and_ids:
  print id,usr
