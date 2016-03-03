
class EmptyQueue(Exception):
  pass

class  priority_queue():
  
  def __init__(self):
    self._q=[ [],[],[],[],[] ]

  def add(self, item , priority = 2):
    if not 0 <= priority < 5 :
      raise ValueError("greater than 5")
    if not isinstance(priority,int):
      raise TypeError("non integers are not allowd")
    try:
      self._q[priority].insert(0,item)
    except:
     raise ValueError("cant insert")
  def pop(self):
    for qu in self._q:
            if qu:
              return qu.pop()
    raise EmptyQueue("pop from empty queue")
  
  def __len__(self):
    return sum(map(len, self._q))
