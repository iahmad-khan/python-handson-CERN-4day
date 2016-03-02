class make_queue:

  def __init__(self):
    self.queue=[]

  def add(self,item):
    self.queue.append(item)

  def pop(self):
    return self.queue.pop(0)

class emerq(make_queue):

  def add1(self,item):
    self.queue.insert(0,item)
    
