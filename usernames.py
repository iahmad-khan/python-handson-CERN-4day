#!/usr/bin/python
import sys

try:
  f = open('/etc/passwd','r')
except Exception as e:
  print e
  sys.exit(1)

users_and_ids = []
for line in f:
  info = line.split(':')
  pair = int(info[3]),(info[0])
  users_and_ids.append(pair)

users_and_ids.sort(key=lambda k:k[0])
for id,usr in users_and_ids:
  print id,usr
