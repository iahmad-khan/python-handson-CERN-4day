class make_queue:

  def __init__(self):
    self._queue=[]

  def add(self,item):
    self._queue.append(item)

  def pop(self):
    return self._queue.pop(0)

class emerq(make_queue):

  def add1(self,item):
    self._queue.insert(0,item)
    
