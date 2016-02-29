#!/usr/bin/python
f=open('/etc/passwd','r')
d={}
for line in f:
  info = line.split(':')
  user,id = info[0],int(info[3])
  d[id] = user
for key in sorted(d):
  print key , d[key]
