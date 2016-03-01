#!/usr/bin/python
import sys

f = open('/etc/passwd','r')

users_and_ids = []

for line in f:
  u,_,id,_ = line.split(':',3)
  pair = int(id),u
  users_and_ids.append(pair)

users_and_ids.sort()
for id,usr in users_and_ids:
  print id,usr
