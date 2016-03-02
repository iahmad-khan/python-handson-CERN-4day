#!/usr/bin/python
class counter:

    def __init__(self, start):
        print dir(self)
        self.count = start
        print dir(self)

    def up(self, n=1):
        self.count += n

    def down(self, n=1):
        self.count -= n
