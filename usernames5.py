#!/usr/bin/python
import sys
f = open('/etc/passwd','r')
users_and_ids = []
for line in f:
  u,_,id,_ = line.split(':',3)
  users_and_ids.append((u,int(id)))
users_and_ids.sort(key = lambda pair:pair[1])
for id,usr in users_and_ids:
  print id,usr


