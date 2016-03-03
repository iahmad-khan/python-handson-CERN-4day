class EmptyQueue(Exception):
  pass

class make_queue:

  def __init__(self):
    self._queue=[]

  def add(self,item):
    self._queue.append(item)

  def pop(self):
    try:
      return self._queue.pop(0)
    except IndexError:
      raise EmptyQueue

class emerq(make_queue):
#special add that adds to the front of queue
  def add2(self,item):
    self._queue.insert(0,item)
    
