#!/usr/bin/python
class counter:

    def __init__(self, start):
        self.count = start
   
    def up(self, n=1):
        self.count += n

    def down(self, n=1):
        self.count -= n

class addcounter(counter):

  def __repr__(self):
    return 'addcounter({.count})'.format(self)

  def __add__(self,other):
    return addcounter(self.count+other.count)

#print addcounter(3) + addcounter(4)
